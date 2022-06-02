# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Define the Games repository.

Classes:
    GamesRepository
"""

from typing import Union
from pymongo.collection import Collection, ObjectId
from ..db.mongodb import mongo_database
from ..models.games import GamesModel, GamesPartialModel


class GamesRepository:
    """Repository to manage Games objects."""

    collection: Collection

    def __init__(self):
        self.collection = mongo_database.get_collection("games")

    async def read(self, game_id: str) -> Union[GamesModel, None]:
        """Read a Games object from the database."""

        game_object = await self.collection.find_one(ObjectId(game_id))
        if game_object:
            return GamesModel(**game_object)

    async def create(self, game: GamesPartialModel) -> GamesModel:
        """Create a Games object."""

        inserted_result = await self.collection.insert_one(dict(game))
        return await self.read(inserted_result.inserted_id)
