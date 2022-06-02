#!/bin/bash
# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)

collections=(maps regions)

for collection in ${collections[@]}
do
    echo "Importing collection: ${collection}..."
    mongoimport \
        --host 127.0.0.1:27017 \
        --db ${MONGO_INITDB_DATABASE} \
        --username ${MONGO_INITDB_ROOT_USERNAME} \
        --password ${MONGO_INITDB_ROOT_PASSWORD} \
        --authenticationDatabase admin \
        --collection ${collection} \
        --jsonArray \
        --type json \
        --file /docker-entrypoint-initdb.d/${collection}.json
done
