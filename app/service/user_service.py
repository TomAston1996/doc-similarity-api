"""
User Service
Author: Tom Aston
"""

from datetime import timedelta

from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import create_access_token, verify_password
from app.core.config import config_manager
from app.errors import (
    InvalidCredentialsException,
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

        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }

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
