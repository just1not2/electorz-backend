# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Define the Games models.

Classes:
    GamesModel
    GamesPartialModel
"""

from pydantic import BaseModel
from .read import ReadModel, ObjectIdType


class GamesModel(ReadModel):
    """Representation of Games in the database."""

    id: ObjectIdType
    mapId: int

class GamesPartialModel(BaseModel):
    """Partial representation of Games."""

    mapId: int
