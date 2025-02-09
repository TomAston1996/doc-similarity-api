"""
Cache module for the application
Author: Tom Aston
"""

import redis.asyncio as redis

from .config import config_manager

jti_blocklist = redis.from_url(
    f"redis://{config_manager.REDIS_HOST}:{config_manager.REDIS_PORT}/0",
    encoding="utf-8",
    decode_responses=True,
)

docs_cache = redis.from_url(
    f"redis://{config_manager.REDIS_HOST}:{config_manager.REDIS_PORT}/1",
    encoding="utf-8",
    decode_responses=True,
)


async def add_jti_to_blocklist(jti: str) -> None:
    """
    Add token to blocklist

    Parameters:
    - jti: str: unique identifier for the token
    """
    await jti_blocklist.set(name=jti, value="", ex=config_manager.JTI_TOKEN_EXPIRY)


async def is_jti_blacklisted(jti: str) -> bool:
    """
    Check if token is blacklisted

    Parameters:
    - jti: str: unique identifier for the token

    Returns:
    - bool: True if token is blacklisted, False otherwise
    """
    return await jti_blocklist.get(jti) is not None


async def add_docs_to_cache(key: str, value: str) -> None:
    """
    Add docs to cache

    Parameters:
    - key: str: key for the cache
    - value: str: value to store in the cache
    """
    await docs_cache.set(name=key, value=value, ex=config_manager.DOCS_CACHE_EXPIRY)


async def is_docs_in_cache(key: str) -> bool:
    """
    Check if docs are in cache

    Parameters:
    - key: str: key for the cache

    Returns:
    - bool: True if docs are in cache, False otherwise
    """
    return await docs_cache.exists(key)


async def get_docs_from_cache(key: str) -> str:
    """
    Get docs from cache

    Parameters:
    - key: str: key for the cache
    """
    return await docs_cache.get(key)
