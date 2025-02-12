"""
Pagination deps for the FastAPI app
Author: Tom Aston
"""

from enum import Enum

from fastapi import Query
from pydantic import BaseModel


class SortEnum(Enum):
    ASC = "asc"
    DESC = "desc"


class Pagination(BaseModel):
    perPage: int
    page: int
    order: SortEnum


def pagination_params(
    page: int = Query(ge=1, required=False, default=1),
    perPage: int = Query(ge=1, le=100, required=False, default=10),
    order: SortEnum = SortEnum.DESC,
) -> Pagination:
    """
    Get pagination parameters

    Parameters:
    - page: int: page number
    - perPage: int: number of items per page
    - order: SortEnum: order of items

    Returns:
    - Pagination: pagination parameters
    """
    return Pagination(perPage=perPage, page=page, order=order)
