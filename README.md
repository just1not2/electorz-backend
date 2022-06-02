# ElectorZ - Backend

ElectorZ is a political game based on geographical strategies.

This repository hosts the backend of the ElectorZ web application, written in [FastAPI](https://fastapi.tiangolo.com). The code of the frontend is available in the [Electorz Frontend repository](https://github.com/just1not2/electorz-frontend).

## Configuration

The entire project configuration is defined in an environment file, of which [a template](./.env.template) is present in the repository. To bootstrap the configuration, launch the following command:

```bash
make .env
```

You may then modify the following environment variables to configure the ElectorZ backend:
* `APP_HOST`: IP address on which the server listens
* `APP_PORT`: port on which the server listens
* `FRONTEND_URL`: URL of the frontend (to enable CORS)
* `MONGO_HOST`: host of the MongoDB instance
* `MONGO_PORT`: port on which the MongoDB instance listens
* `MONGO_DB_NAME`: name of the MongoDB database
* `MONGO_USERNAME`: name of the MongoDB user
* `MONGO_PASSWORD`: password of the MongoDB user
* `MONGO_TLS`: boolean that indicates if TLS must be enabled to connect to the MongoDB instance
* `MONGO_MAX_CONNECTIONS`: maximum number of connections to the MongoDB instance
* `MONGO_MIN_CONNECTIONS`: minimum number of connections to the MongoDB instance


## Installation

You can install the `pip` requirements by launching the following command:

```bash
make install
```

### MongoDB instance

If you do not have a MongoDB instance available for the ElectorZ application, you can launch a dockerized version of MongoDB by launching the following command:

```bash
make stack
```

It will automatically provision the database with the JSON files present in the [db-init directory](./db-init/).

Note that a `mongo-express` image has been added to the [docker-compose file](./docker-compose.yml) to help you manage the database: it provides a web administration tool available at http://localhost:8081.


## Launching the application

Once a MongoDB database is available with the configuration options provided in the environment file, the ElectorZ backend application may be launched with the following command:

```bash
make start
```


## Documentation

FastAPI provides automatic documentations thanks to the [Swagger & Redoc modules](https://fastapi.tiangolo.com/tutorial/metadata/): you can for instance visit http://localhost:8080/docs to get all information about the API and test the routes.


## See Also

* [FastAPI official documentation](https://fastapi.tiangolo.com)
* [PyMongo documentation](https://pymongo.readthedocs.io/en/stable/)


## Contributing to this application

This application started as personal project, but I welcome community contributions to it. If you find problems, please open an issue or create a PR against the [ElectorZ Backend repository](https://github.com/just1not2/electorz-backend).

You can also reach me by email at `me@just1not2.org`.


## Licensing

Mozilla Public License Version 2.0.

See [LICENSE](./LICENSE) to see the full text.


## Author Information

This application was created in 2022 by Justin Béra.