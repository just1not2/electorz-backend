# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Define the Regions router.

Functions:
    get_regions_route

Variables:
    regions_router
"""

from fastapi import APIRouter, Path, status
from fastapi.responses import JSONResponse
from pydantic import Required
from ..models.regions import RegionsModel
from ..repositories.regions import RegionsRepository


regions_router = APIRouter(tags=["regions"])

@regions_router.get(
    path="/{region_id}",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "model": RegionsModel,
            "description": "Region successfully returned",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Region not found",
        },
    },
    summary="read a region",
    description="Read a specific region",
)
async def get_regions_route(region_id: int = Path(
    default=Required,
    title="Region ID",
    description="ID of the region",
    example="18",
)) -> bytes:
    """Route to read a region."""

    regions_repository = RegionsRepository()

    region = await regions_repository.read(region_id)
    if region:
        return JSONResponse(content=dict(region), status_code=status.HTTP_200_OK)
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
