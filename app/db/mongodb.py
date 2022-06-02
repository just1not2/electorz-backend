# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Initialize the MongoDB connector.

Classes:
    MongoDB

Variables:
    mongo_database
"""

from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_tornado import MotorDatabase
from pymongo.collection import Collection
from .settings import MONGO_DB_NAME, MONGO_MAX_CONNECTIONS, MONGO_MIN_CONNECTIONS, MONGO_URI


class MongoDB:
    """Representation of a MongoDB connector."""

    client: AsyncIOMotorClient
    database: MotorDatabase

    async def connect(self):
        """Initialize the connection to the MongoDB instance."""

        # Create the MongoDB client
        self.client = AsyncIOMotorClient(
            MONGO_URI,
            maxPoolSize=MONGO_MAX_CONNECTIONS,
            minPoolSize=MONGO_MIN_CONNECTIONS,
        )

        # Get the database
        self.database = self.client.get_database(MONGO_DB_NAME)
        print(f"Connected to MongoDB at URI {MONGO_URI}")

    async def close(self):
        """Close the connection to the MongoDB instance."""

        self.client.close()
        print("Closed connection with MongoDB")

    def get_collection(self, collection: str) -> Collection:
        """Get a specific MongoDB collection."""

        return self.database.get_collection(collection)

mongo_database = MongoDB()
