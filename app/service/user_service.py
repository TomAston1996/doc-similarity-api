"""
User Service
Author: Tom Aston
"""

import logging
from datetime import datetime, timedelta

from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import create_access_token, verify_password
from app.core.cache import add_jti_to_blocklist
from app.core.config import config_manager
from app.errors import (
    InvalidCredentialsException,
    InvalidTokenException,
    UserAlreadyExistsException,
    UserNotFoundException,
)
from app.models.user import User
from app.repository.user_repository import UserRepository
from app.schema.user_schema import (
    UserClientResponse,
    UserCreateClientRequest,
    UserLoginRequest,
)

user_repository = UserRepository()
logger = logging.getLogger("uvicorn")


class UserService:
    """
    user service class
    """

    async def get_by_email(self, email: str, db: AsyncSession) -> UserClientResponse:
        """
        service for getting a user by email
        """
        repository_response: User | None = await user_repository.get_by_email(email, db)

        if not repository_response:
            raise UserNotFoundException()

        return repository_response

    async def create_user(
        self, user_create_request: UserCreateClientRequest, db: AsyncSession
    ) -> UserClientResponse:
        """
        service for creating a user
        """

        if await user_repository.get_by_email(user_create_request.email, db):
            raise UserAlreadyExistsException()

        if await user_repository.get_by_username(user_create_request.username, db):
            raise UserAlreadyExistsException()

        db_user: User = await user_repository.create_user(user_create_request, db)

        client_response = UserClientResponse(**db_user.__dict__)

        return client_response

    async def get_all(self, db: AsyncSession) -> list[UserClientResponse]:
        """
        service for getting all users
        """
        repository_response: list[User] | None = await user_repository.get_all(db)

        if not repository_response:
            return []

        return repository_response

    async def login_user(
        self, user_login_data: UserLoginRequest, db: AsyncSession
    ) -> JSONResponse:
        """
        service for logging in a user
        """
        user: User = await user_repository.get_by_email(user_login_data.email, db)

        # 1. Check if user exists
        if not user:
            raise InvalidCredentialsException()

        # 2. Check if password is correct
        if not verify_password(user_login_data.password, user.password_hash):
            raise InvalidCredentialsException()

        user_data = {"id": user.id, "username": user.username, "email": user.email}

        # 3. Create access token
        access_token = create_access_token(user_data=user_data)

        # 4. Create refresh token
        refresh_token = create_access_token(
            user_data=user_data,
            refresh=True,
            expiry=timedelta(seconds=config_manager.REFRESH_TOKEN_EXPIRY),
        )

        return JSONResponse(
            content={
                "message": "Login successful",
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user": user_data,
            }
        )

    async def refresh_token(self, token: dict) -> JSONResponse:
        """
        service for refreshing a token
        """
        expiry_timestamp = token.get("exp")
        expiry_datetime = datetime.fromtimestamp(expiry_timestamp)

        # 1. Check if token is expired
        if expiry_datetime < datetime.now():
            raise InvalidTokenException()

        # 2. Create new access token
        access_token = create_access_token(user_data=token["user"])

        return JSONResponse(
            content={"message": "Token refreshed", "access_token": access_token},
            status_code=200,
        )

    async def logout_user(self, token: dict) -> JSONResponse:
        """
        service for logging out a user
        """
        # revokee the token jti
        await add_jti_to_blocklist(token["jti"])

        return JSONResponse(
            content={"message": "Logout successful"}, status_code=status.HTTP_200_OK
        )
