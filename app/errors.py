"""
This module contains all the custom exceptions that are raised in the Bookly App
Author: Tom Aston
"""

from typing import Any, Callable

from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse


class AppException(Exception):
    """
    Base class for all custom exceptions in the Bookly App
    """

    pass


class DocumentNotFoundException(AppException):
    """
    Raised when a document is not found in the database
    """

    pass


class UserNotFoundException(AppException):
    """
    Raised when a user is not found in the database
    """

    pass


class UserAlreadyExistsException(AppException):
    """
    Raised when a user already exists in the database
    """

    pass


class InvalidCredentialsException(AppException):
    """
    Raised when the user provides invalid credentials
    """

    pass

class InvalidTokenException(AppException):
    """
    Raised when the user provides an invalid token
    """

    pass

class AccessTokenException(AppException):
    """
    Raised when the user provides an invalid access token
    """

    pass


class RefreshTokenException(AppException):
    """
    Raised when the user provides an invalid refresh token
    """

    pass


def create_exception_hander(
    status_code: int, detail: Any
) -> Callable[[Request, Exception], JSONResponse]:
    """
    Factory function that creates an exception handler for a given status code and detail
    """

    async def exception_handler(request: Request, exc: AppException) -> JSONResponse:
        """
        Exception handler for a given status code and detail
        """
        return JSONResponse(
            status_code=status_code,
            content={"message": str(detail)},
        )

    return exception_handler


def register_all_errors(app: FastAPI) -> None:
    """
    Registers all the custom exceptions in the Bookly App
    """
    app.add_exception_handler(
        DocumentNotFoundException,
        create_exception_hander(
            status.HTTP_404_NOT_FOUND, "Document title or id not found"
        ),
    )
    app.add_exception_handler(
        UserNotFoundException,
        create_exception_hander(
            status.HTTP_404_NOT_FOUND, "User email or id not found"
        ),
    )
    app.add_exception_handler(
        UserAlreadyExistsException,
        create_exception_hander(
            status.HTTP_409_CONFLICT, "User email or username already exists"
        ),
    )
    app.add_exception_handler(
        InvalidCredentialsException,
        create_exception_hander(
            status.HTTP_401_UNAUTHORIZED, "Password or email is invalid"
        ),
    )
    app.add_exception_handler(
        InvalidTokenException,
        create_exception_hander(
            status.HTTP_401_UNAUTHORIZED, "Invalid token"
        ),
    )
    app.add_exception_handler(
        AccessTokenException,
        create_exception_hander(
            status.HTTP_401_UNAUTHORIZED, "Access token is invalid"
        ),
    )
    app.add_exception_handler(
        RefreshTokenException,
        create_exception_hander(
            status.HTTP_401_UNAUTHORIZED, "Refresh token is invalid"
        ),
    )
