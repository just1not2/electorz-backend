# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Define the main router.

Variables:
    main_router
"""

from fastapi import APIRouter
from .games import games_router
from .maps import maps_router
from .regions import regions_router


# Define the main router
main_router = APIRouter()

# Add secondary routers
main_router.include_router(router=games_router, prefix="/games")
main_router.include_router(router=maps_router, prefix="/maps")
main_router.include_router(router=regions_router, prefix="/regions")
