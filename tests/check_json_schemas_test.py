import pytest
from pre_commit_hooks.check_json_schemas import main


def test_valid_schemas(valid_set_of_files):
    args = valid_set_of_files
    assert main(args) == 0

def test_invalid_schemas(invalid_set_of_files):
    args = invalid_set_of_files
    assert main(args) == 1

