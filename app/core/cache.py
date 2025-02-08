"""
Cache module for the application
Author: Tom Aston
"""

import redis.asyncio as redis

from .config import config_manager

token_blocklist = redis.from_url(
    f"redis://{config_manager.REDIS_HOST}:{config_manager.REDIS_PORT}/0",
    encoding="utf-8",
    decode_responses=True,
)


async def add_jti_to_blocklist(jti: str) -> None:
    """
    Add token to blocklist

    Parameters:
    - jti: str: unique identifier for the token
    """
    await token_blocklist.set(name=jti, value="", ex=config_manager.JTI_TOKEN_EXPIRY)


async def is_jti_blacklisted(jti: str) -> bool:
    """
    Check if token is blacklisted

    Parameters:
    - jti: str: unique identifier for the token

    Returns:
    - bool: True if token is blacklisted, False otherwise
    """
    return await token_blocklist.get(jti) is not None
