"""
User Router
Author: Tom Aston
"""

from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import database
from app.schema.user_schema import (
    UserClientResponse,
    UserCreateClientRequest,
    UserLoginRequest,
)
from app.service.user_service import UserService

user_router = APIRouter()
user_service = UserService()


@user_router.post(
    "/signup", response_model=UserClientResponse, status_code=status.HTTP_201_CREATED
)
async def signup_user(
    user_create_request: UserCreateClientRequest,
    db: Annotated[AsyncSession, Depends(database.get_db)],
) -> UserClientResponse:
    """
    POST signup user endpoint
    """
    return await user_service.create_user(
        user_create_request=user_create_request, db=db
    )


@user_router.get(
    "/{email}", response_model=UserClientResponse, status_code=status.HTTP_200_OK
)
async def get_user_by_email(
    email: str, db: Annotated[AsyncSession, Depends(database.get_db)]
) -> UserClientResponse:
    """
    GET a user by email endpoint
    """
    return await user_service.get_by_email(email=email, db=db)


@user_router.get(
    "/", response_model=list[UserClientResponse], status_code=status.HTTP_200_OK
)
async def get_all_users(
    db: Annotated[AsyncSession, Depends(database.get_db)],
) -> list[UserClientResponse]:
    """
    GET all users endpoint
    """
    return await user_service.get_all(db=db)


@user_router.post("/login", status_code=status.HTTP_200_OK)
async def login_user(
    user_login_data: UserLoginRequest,
    db: Annotated[AsyncSession, Depends(database.get_db)],
) -> JSONResponse:
    """
    POST login user endpoint
    """
    return await user_service.login_user(user_login_data, db)


# @user_router.get("/refresh", status_code=status.HTTP_200_OK)
# async def get_new_access_token() -> JSONResponse:
#     """
#     GET refresh token endpoint
#     """
#     return await user_service.refresh_token()
