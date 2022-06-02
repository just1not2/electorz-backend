# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Define the Regions repository.

Classes:
    RegionsRepository
"""

from typing import Union
from pymongo.collection import Collection
from ..db.mongodb import mongo_database
from ..models.regions import RegionsModel


class RegionsRepository:
    """Repository to manage Regions objects."""

    collection: Collection

    def __init__(self):
        self.collection = mongo_database.get_collection("regions")

    async def read(self, region_id: int) -> Union[RegionsModel, None]:
        """Read a Regions object from the database."""

        region_object = await self.collection.find_one(region_id)
        if region_object:
            return RegionsModel(**region_object)
