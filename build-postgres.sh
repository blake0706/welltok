#!/bin/sh

echo "Creating user np_db_user"
createuser -U postgres -h localhost -d -s np_db_user
echo "Creating database np_db"
createdb -U postgres -h localhost -O np_db_user np_db
echo "Creating database test"
createdb -U postgres -h localhost -O np_db_user test
