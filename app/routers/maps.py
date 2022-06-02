# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Define the Maps router.

Functions:
    get_maps_route

Variables:
    maps_router
"""

from fastapi import APIRouter, Path, status
from fastapi.responses import JSONResponse
from pydantic import Required
from ..models.maps import MapsModel
from ..repositories.maps import MapsRepository


maps_router = APIRouter(tags=["maps"])

@maps_router.get(
    path="/{map_id}",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "model": MapsModel,
            "description": "Map successfully returned",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Map not found",
        },
    },
    summary="read a map",
    description="Read a specific map",
)
async def get_maps_route(map_id: int = Path(
    default=Required,
    title="Map ID",
    description="ID of the map",
    example="1",
)) -> bytes:
    """Route to read a map."""

    maps_repository = MapsRepository()

    map_object = await maps_repository.read(map_id)
    if map_object:
        return JSONResponse(content=dict(map_object), status_code=status.HTTP_200_OK)
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
