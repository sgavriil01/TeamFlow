"""Test configuration for pytest."""

import pytest
from fastapi.testclient import TestClient
from teamflow.main import app


@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app)
