#!/bin/bash
set -e
dropdb -h localhost --if-exists -U np_db_user test
dropdb -h localhost --if-exists -U np_db_user np_db

./build-postgres.sh
