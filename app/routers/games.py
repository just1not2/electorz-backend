# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Define the Games router.

Functions:
    get_games_route
    post_games_route

Variables:
    games_router
"""

from fastapi import APIRouter, Body, Path, status
from fastapi.responses import JSONResponse
from pydantic import Required
from ..models.read import ObjectIdType
from ..models.games import GamesModel, GamesPartialModel
from ..repositories.games import GamesRepository


games_router = APIRouter(tags=["games"])

@games_router.get(
    path="/{game_id}",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "model": GamesModel,
            "description": "Game successfully returned",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Game not found",
        },
    },
    summary="read a game",
    description="Read a specific game",
)
async def get_games_route(game_id: ObjectIdType = Path(
    default=Required,
    title="Game ID",
    description="ID of the game",
    example="62979db2dcf0f1fb07d4a7b3",
)) -> bytes:
    """Route to read a game."""

    games_repository = GamesRepository()

    game = await games_repository.read(game_id)
    if game:
        return JSONResponse(content=dict(game), status_code=status.HTTP_200_OK)
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)

@games_router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "model": GamesModel,
            "description": "Game successfully created",
        },
    },
    summary="create a game",
    description="Create a game from a partial game object",
)
async def post_games_route(game_partial_object: GamesPartialModel = Body(
    default=Required,
    title="Partial game object",
    description="Partial game object that will be created",
    example=GamesPartialModel(
        mapId=1,
    ),
)) -> bytes:
    """Route to create a game."""

    games_repository = GamesRepository()

    game = await games_repository.create(game_partial_object)
    return JSONResponse(content=dict(game), status_code=status.HTTP_201_CREATED)
