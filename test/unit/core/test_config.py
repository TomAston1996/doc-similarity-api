"""
Config Unit Test
Author: Tom Aston
"""

from app.core.config import ConfigManager


def test_config_db_parameters(config: ConfigManager):
    """
    Test config manager params are present
    """
    assert config.POSTGRES_DB is not None
    assert config.POSTGRES_HOST_NAME is not None
    assert config.POSTGRES_HOST_PORT is not None
    assert config.POSTGRES_PASSWORD is not None
    assert config.POSTGRES_USER is not None
