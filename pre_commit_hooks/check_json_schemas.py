from __future__ import annotations
from typing import Sequence
import argparse
import json
from fastjsonschema import compile, JsonSchemaDefinitionException, JsonSchemaException

def main(argv: Sequence[str] | None = None) -> int:
    retval = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    for filename in args.filenames:
        try:
            with open(filename, 'rb') as f:
                schema = json.load(f)
                compile(schema)
        except JsonSchemaDefinitionException as e:
            print(f'{filename}: invalid schema: {e}')
            retval = 1
        except JsonSchemaException:
            None
    return retval

if __name__ == '__main__':
    raise SystemExit(main())