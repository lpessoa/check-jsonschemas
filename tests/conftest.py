import pytest


@pytest.fixture
def valid_set_of_files():
    return [
        "fixtures/valid-schemas/draft-03.json",
        "fixtures/valid-schemas/draft-04.json",
        "fixtures/valid-schemas/draft-06.json",
        "fixtures/valid-schemas/draft-07.json",
        "fixtures/valid-schemas/draft-201909.json",
        "fixtures/valid-schemas/draft-202012.json",
    ]


@pytest.fixture
def invalid_set_of_files():
    return [
        "fixtures/invalid-schemas/without-schema-entry.json",
        "fixtures/invalid-schemas/draft-03.json",
        "fixtures/invalid-schemas/draft-04.json",
        "fixtures/invalid-schemas/draft-06.json",
        "fixtures/invalid-schemas/draft-07.json",
        "fixtures/invalid-schemas/draft-201909.json",
        "fixtures/invalid-schemas/draft-202012.json",
    ]
