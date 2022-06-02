# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Define the Regions models.

Classes:
    RegionsModel
"""

from typing import Dict, List
from .read import ReadModel


class RegionsModel(ReadModel):
    """Representation of Regions in the database."""

    id: str
    name: str
    code: str
    electors: int
    shape: List[List[Dict[str, float]]]
