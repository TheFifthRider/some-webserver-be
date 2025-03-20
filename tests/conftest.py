import pytest

from fastapi.testclient import TestClient

from some_webserver.main import initialize, Settings
from tests.fakers import _test_faker, TestFaker


@pytest.fixture(scope="session")
def test_client() -> TestClient:
    test_settings = Settings(db_url = "sqlite:///:memory:", commit_on_exit = False)
    app, _ = initialize(test_settings)
    return TestClient(app)

@pytest.fixture
def test_faker() -> TestFaker:
    return _test_faker
