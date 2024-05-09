import os
from pathlib import Path
import pytest


@pytest.fixture
def valid_set_of_files(request: pytest.FixtureRequest):
    folder = Path(os.path.dirname(request.path))
    return [
        item.as_posix()
        for item in [
            folder / "fixtures/valid-schemas/draft-03.json",
            folder / "fixtures/valid-schemas/draft-04.json",
            folder / "fixtures/valid-schemas/draft-06.json",
            folder / "fixtures/valid-schemas/draft-07.json",
            folder / "fixtures/valid-schemas/draft-201909.json",
            folder / "fixtures/valid-schemas/draft-202012.json",
        ]
    ]


@pytest.fixture
def invalid_set_of_files(request: pytest.FixtureRequest):
    folder = Path(os.path.dirname(request.path))
    return [
        item.as_posix()
        for item in [
            folder / "fixtures/invalid-schemas/without-schema-entry.json",
            folder / "fixtures/invalid-schemas/draft-03.json",
            folder / "fixtures/invalid-schemas/draft-04.json",
            folder / "fixtures/invalid-schemas/draft-06.json",
            folder / "fixtures/invalid-schemas/draft-07.json",
            folder / "fixtures/invalid-schemas/draft-201909.json",
            folder / "fixtures/invalid-schemas/draft-202012.json",
        ]
    ]
