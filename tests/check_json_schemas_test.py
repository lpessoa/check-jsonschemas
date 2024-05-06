from pre_commit_hooks.check_json_schemas import main


def test_valid_schemas(valid_set_of_files):
    for arg in valid_set_of_files:
        print(f': [test_valid_schemas] assert if {arg} is a valid schema-file')
        assert main([arg]) == 0


def test_all_valid_schema_files(valid_set_of_files):
    print(f': [test_all_valid_schema_files] assert if all schema-files are valid')
    args = valid_set_of_files
    assert main(args) == 0


def test_invalid_schemas(invalid_set_of_files):
    for arg in invalid_set_of_files:
        print(f': [test_invalid_schemas] assert if {arg} is a invalid schema-file')
        assert main([arg]) == 1


def test_all_invalid_schemas(invalid_set_of_files):
    print(f': [test_all_invalid_schemas] assert if all schema-files are invalid')
    args = invalid_set_of_files
    assert main(args) == 1
