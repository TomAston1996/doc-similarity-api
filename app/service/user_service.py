"""
User Service
Author: Tom Aston
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repository.user_repository import UserRepository
from app.schema.user_schema import UserClientResponse, UserCreateClientRequest
from app.errors import UserNotFoundException, UserAlreadyExistsException

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
