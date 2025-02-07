"""
Document Repository Layer
Author: Tom Aston
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from app.core.auth import generate_password_hash
from app.models.user import User
from app.schema.user_schema import UserCreateClientRequest


class UserRepository:
    """
    user repository class
    """

    async def get_all(self, db: AsyncSession) -> list[User] | None:
        """
        get all users
        """
        statement = select(User).order_by(User.id)
        result = await db.execute(statement)
        return result.scalars().all()

    async def get_by_email(self, email: str, db: AsyncSession) -> User | None:
        """
        get a user by email
        """
        statement = select(User).where(User.email == email)
        result = await db.execute(statement)
        return result.scalars().first()

    async def get_by_username(self, username: str, db: AsyncSession) -> User | None:
        """
        get a user by username
        """
        statement = select(User).where(User.username == username)
        result = await db.execute(statement)
        return result.scalars().first()

    async def user_exists(self, email: str, db: AsyncSession) -> bool:
        """
        check if a user exists by email
        """
        user = self.get_by_email(email, db)
        return user is not None

    async def create_user(
        self, user_create_request: UserCreateClientRequest, db: AsyncSession
    ) -> User:
        """
        create a user
        """
        user = User(**user_create_request.model_dump(exclude={"password"}))
        user.password_hash = generate_password_hash(user_create_request.password)
        db.add(user)
        await db.commit()
        return user
