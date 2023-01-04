import json
from pathlib import Path
from typing import Any, Dict

import pytest


@pytest.fixture
def test_schema_path() -> str:
    return Path(__file__).parent.joinpath("./tests.json").as_posix()


@pytest.fixture
def json_data(test_schema_path) -> Dict[str, Any]:  # type: ignore
    return json.loads(test_schema_path)
