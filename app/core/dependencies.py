"""
Dependencies for the FastAPI app
Author: Tom Aston
"""

import logging

from fastapi import Depends, Request
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import database
from app.core.cache import is_jti_blacklisted
from app.errors import (
    AccessTokenException,
    InvalidTokenException,
    RefreshTokenException,
)
from app.service.user_service import UserService

from .auth import decode_token

user_service = UserService()
logger = logging.getLogger('uvicorn')

class TokenBearer(HTTPBearer):
    """
    Access token bearer class
    """

    def __init__(self, auto_error: bool = True):
        """
        Override the __init__ method and set auto_error to True
        """
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        """
        Override the __call__ method
        """
        credentials = await super().__call__(request)

        # credentials.credentials are the token itself i.e. the JWT token itself with header and payload
        token = credentials.credentials

        if not self.validate_token(token):
            raise InvalidTokenException()

        token_data = decode_token(token)

        if await is_jti_blacklisted(token_data["jti"]):
            raise InvalidTokenException()

        self.verify_token_data(token_data)

        return token_data

    def validate_token(self, token: str) -> bool:
        """
        Validate the token

        Parameters:
        - token: str: JWT token

        Returns:
        - bool: True if token is valid, False otherwise
        """
        token_data = decode_token(token)
        return token_data is not None

    def verify_token_data(self, token_data: dict) -> None:
        """
        Verify token data

        Parameters:
        - token_data: dict: token data

        Returns:
        - None
        """
        raise NotImplementedError("Method not implemented")


class AccessTokenBearer(TokenBearer):
    """
    Access token bearer class
    """

    def verify_token_data(self, token_data: dict) -> None:
        """
        Verify token data

        Parameters:
        - token_data: dict: token data

        Throws:
        - throws HTTPException if token is a refresh token
        """
        # refresh flag is a boolean value that indicates if the token is a refresh token
        if token_data and token_data["refresh"]:
            raise AccessTokenException()


class RefreshTokenBearer(TokenBearer):
    """
    Refresh token bearer class that inherits from TokenBearer
    """

    def verify_token_data(self, token_data: dict) -> None:
        """
        Verify token data

        Parameters:
        - token_data: dict: token data

        Returns:
        - throws HTTPException if token is not a  refresh token
        """
        # refresh flag is a boolean value that indicates if the token is a refresh token
        if token_data and not token_data["refresh"]:
            raise RefreshTokenException()


async def get_current_user(
    token: dict = Depends(AccessTokenBearer()),
    db: AsyncSession = Depends(database.get_db),
) -> dict:
    """
    Get the current user

    Parameters:
    - token: dict: token data

    Returns:
    - dict: user data
    """
    user_email = token["user"]["email"]
    user = await user_service.get_by_email(email=user_email, db=db)
    return user
