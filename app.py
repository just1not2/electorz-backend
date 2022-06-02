# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)
"""
Launch the ElectorZ application.

Variables:
    APP_HOST
    APP_PORT
"""

import os
import dotenv
import uvicorn


# Load the `.env` file
dotenv.load_dotenv()

# Define global app parameters
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", "8080"))

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", host=APP_HOST, port=APP_PORT, log_level="debug", reload=True
    )
