from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from src.main.app import server


@pytest.fixture(scope="module")
def client() -> Generator[TestClient]:
    with TestClient(server) as c:
        yield c
