# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Initialize the ElectorZ FastAPI application.

Functions:
    close_mongo_database
    connect_mongo_database

Variables:
    app
    FRONTEND_URL
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db.mongodb import mongo_database
from .routers.main import main_router


app = FastAPI(
    title="ElectorZ",
    description="Backend of the ElectorZ application.",
    version="0.1.0",
    contact={
        "name": "Justin Béra",
        "url": "https://github.com/just1not2/",
        "email": "me@just1not2.org",
    },
    license_info={
        "name": "Mozilla Public License Version 2.0",
        "url": "https://www.mozilla.org/en-US/MPL/2.0/",
    },
)

# Enable Cross-Origin Requests from the frontend
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://127.0.0.1:3000")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def connect_mongo_database():
    """Event to initialize the connection to the MongoDB instance."""

    await mongo_database.connect()

@app.on_event("shutdown")
async def close_mongo_database():
    """Event to close the connection to the MongoDB instance."""

    await mongo_database.close()

# Attach routes to the FastAPI app
app.include_router(main_router, prefix="")
