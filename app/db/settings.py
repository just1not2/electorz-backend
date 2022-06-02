# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Set MongoDB parameters.

Variables:
    MONGO_DB_NAME
    MONGO_HOST
    MONGO_MAX_CONNECTIONS
    MONGO_MIN_CONNECTIONS
    MONGO_PASSWORD
    MONGO_PORT
    MONGO_TLS
    MONGO_URI
    MONGO_USERNAME
"""

import os


MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_USERNAME = os.getenv("MONGO_USERNAME", "electorz")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "electorz")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "electorz")
MONGO_TLS = os.getenv("MONGO_TLS", "false")
MONGO_MAX_CONNECTIONS = os.getenv("MONGO_MAX_CONNECTIONS", "10")
MONGO_MIN_CONNECTIONS = os.getenv("MONGO_MIN_CONNECTIONS", "10")

# URI options are available at
# https://www.mongodb.com/docs/manual/reference/connection-string/#connection-string-options
MONGO_URI = (
    "mongodb://"
    + f"{MONGO_USERNAME}:{MONGO_PASSWORD}@"
    + f"{MONGO_HOST}:{MONGO_PORT}/"
    + f"?tls={MONGO_TLS}"
)
