"""
auth helper functions
Author: Tom Aston
"""

import logging
import uuid
from datetime import datetime, timedelta

import jwt
from passlib.context import CryptContext

from .config import config_manager

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_EXPIRY = 3600  # 1 hour


def generate_password_hash(password: str) -> str:
    """
    Generate a password hash
    """
    return password_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password hash

    Returns:
        True if the password is correct, False otherwise
    """
    return password_context.verify(plain_password, hashed_password)


def create_access_token(
    user_data: dict, expiry: timedelta = None, refresh: bool = False
) -> str:
    """
    Create an access token

    payload attributes:
    - user: user data
    - exp: expiry time
    - jti: unique identifier for the token
    - refresh: flag to indicate if token is a refresh token
    """
    payload = {}

    payload["user"] = user_data
    payload["exp"] = (
        datetime.now() + expiry
        if expiry
        else datetime.now() + timedelta(seconds=ACCESS_TOKEN_EXPIRY)
    )
    payload["jti"] = str(uuid.uuid4())  # unique identifier for the token
    payload["refresh"] = refresh  # flag to indicate if token is a refresh token

    token = jwt.encode(
        payload=payload,
        key=config_manager.JWT_SECRET,
        algorithm=config_manager.JWT_ALGORITHM,
    )

    return token


def decode_token(token: str) -> dict:
    """
    decode token

    try-except block is used to catch any exception that may occur while decoding the token
    """
    try:
        token_data = jwt.decode(
            jwt=token,
            key=config_manager.JWT_SECRET,
            algorithms=[config_manager.JWT_ALGORITHM],
        )
        return token_data
    except jwt.PyJWTError as e:
        logging.exception(f"Error decoding token: {e}")
        return None
