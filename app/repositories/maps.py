# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Define the Maps repository.

Classes:
    MapsRepository
"""

from typing import Union
from pymongo.collection import Collection
from ..db.mongodb import mongo_database
from ..models.maps import MapsModel


class MapsRepository:
    """Repository to manage Maps objects."""

    collection: Collection

    def __init__(self):
        self.collection = mongo_database.get_collection("maps")

    async def read(self, map_id: int) -> Union[MapsModel, None]:
        """Read a Maps object from the database."""

        map_object = await self.collection.find_one(map_id)
        if map_object:
            return MapsModel(**map_object)
