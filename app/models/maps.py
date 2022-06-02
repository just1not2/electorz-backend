# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Define the Maps models.

Classes:
    MapsModel
"""

from typing import List
from .read import ReadModel


class MapsModel(ReadModel):
    """Representation of Maps in the database."""

    id: str
    title: str
    initialZoom: int
    maxZoom: int
    minZoom: int
    regions: List[int]
