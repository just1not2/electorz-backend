# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Define the base of read models.

Classes:
    ReadModel

Variables:
    ObjectIdType
"""

from pydantic import BaseModel, constr


class ReadModel(BaseModel):
    """Representation of abstract read objects."""

    def __init__(self, **object_dict):
        # The "_id" value is replaced by a deconstructed "id" value
        object_values = { key: value for key, value in object_dict.items() if key != "_id" }
        object_values["id"] = str(object_dict["_id"])

        super().__init__(**object_values)

# Define the type for MongoDB object ID strings before conversion
ObjectIdType = constr(regex=r"^[a-fA-F\d]{24}$")
