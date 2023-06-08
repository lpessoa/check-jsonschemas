from __future__ import annotations
from jsonschema import validate, SchemaError, ValidationError
from typing import Sequence
import argparse
import json

def main(argv: Sequence[str] | None = None) -> int:
    retval = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    for filename in args.filenames:
        try:
            with open(filename, 'rb') as f:
                validate(instance={}, schema=json.load(f))
        except SchemaError as e:
            print(f'{filename}: invalid schema: {e}')
            retval = 1
        except ValidationError:
            None
    return retval

if __name__ == '__main__':
    raise SystemExit(main())