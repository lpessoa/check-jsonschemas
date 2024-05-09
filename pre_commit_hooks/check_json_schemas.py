from __future__ import annotations

import argparse
import json
from typing import Sequence

from jsonschema.validators import (
    Draft7Validator,
    Draft3Validator,
    Draft4Validator,
    Draft6Validator,
    Draft201909Validator,
    Draft202012Validator,
)
from jsonschema.exceptions import SchemaError

SCHEMA = "$schema"


def main(argv: Sequence[str] | None = None) -> int:
    retval = 0
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check.")
    args = parser.parse_args(argv)

    for filename in args.filenames:
        try:
            with open(filename, "rb") as f:
                schema = json.load(f)
                if SCHEMA not in schema:
                    print(
                        f"{filename}: invalid schema, because there is not an entry with $schema in json file"
                    )
                    retval = 1
                    continue
                schemaRef = schema.get(SCHEMA)
                # we are not using the match statement here because we want to support python 3.6
                if Draft3Validator.META_SCHEMA[SCHEMA] in schemaRef:
                    Draft3Validator.check_schema(schema)
                elif Draft4Validator.META_SCHEMA[SCHEMA] in schemaRef:
                    Draft4Validator.check_schema(schema)
                elif Draft6Validator.META_SCHEMA[SCHEMA] in schemaRef:
                    Draft6Validator.check_schema(schema)
                elif Draft201909Validator.META_SCHEMA[SCHEMA] in schemaRef:
                    Draft201909Validator.check_schema(schema)
                elif Draft202012Validator.META_SCHEMA[SCHEMA] in schemaRef:
                    Draft202012Validator.check_schema(schema)
                elif Draft7Validator.META_SCHEMA[SCHEMA] in schemaRef:
                    Draft7Validator.check_schema(schema)
                else:
                    print(
                        f"{filename}: invalid json schema version set in $schema attribute: {schemaRef}"
                    )
                    retval = 1

        except SchemaError as e:
            print(f"{filename}: invalid schema: {e}")
            retval = 1

    return retval


if __name__ == "__main__":
    raise SystemExit(main())
