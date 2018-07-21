from falcon import testing
import pytest

from app import api


@pytest.fixture()
def client():
    return testing.TestClient(api)
