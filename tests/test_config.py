"""Test the configuration module."""

from teamflow.core.config import Settings


def test_settings_creation():
    """Test that settings can be created."""
    settings = Settings()
    assert settings.debug is not None
    assert settings.secret_key is not None


def test_settings_with_env():
    """Test settings loading from environment."""
    settings = Settings(debug=True, secret_key="test-key")
    assert settings.debug is True
    assert settings.secret_key == "test-key"
