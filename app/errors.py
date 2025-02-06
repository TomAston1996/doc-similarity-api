'''
This module contains all the custom exceptions that are raised in the Bookly App
Author: Tom Aston
'''

from typing import Any, Callable
from fastapi.requests import Request
from fastapi import status, FastAPI
from fastapi.responses import JSONResponse

class AppException(Exception):
    '''
    Base class for all custom exceptions in the Bookly App
    '''
    pass

class DocumentNotFoundException(AppException):
    '''
    Raised when a document is not found in the database
    '''
    pass

def create_exception_hander(status_code: int, detail: Any) -> Callable[[Request, Exception], JSONResponse]:
    '''
    Factory function that creates an exception handler for a given status code and detail
    '''
    async def exception_handler(request: Request, exc: AppException) -> JSONResponse:
        '''
        Exception handler for a given status code and detail
        '''
        return JSONResponse(
            status_code=status_code,
            content={"message": str(detail)},
        )
    return exception_handler

def register_all_errors(app: FastAPI) -> None:
    '''
    Registers all the custom exceptions in the Bookly App
    '''
    app.add_exception_handler(DocumentNotFoundException, create_exception_hander(status.HTTP_404_NOT_FOUND, "Document id not found"))