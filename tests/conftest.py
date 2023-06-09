import pytest

@pytest.fixture
def build_content(tmp_path):
    def inner(contents):
        files = []
        count = 0
        for content in contents:
            f = tmp_path/ str(count)
            f.write_text(content)
            files.append(str(f))
            count = count + 1
        return files
    return inner

@pytest.fixture
def valid_set_of_files(build_content):
    return build_content(["""{"format": "date-time"}""", """{"format": "date"}"""])


@pytest.fixture
def invalid_set_of_files(build_content):
    return build_content(["""{"format": "invalid="}"""])
