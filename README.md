# An initial implementation of Django REST api

This is a fun project trying to play around Django REST api framework. To run it follow steps as below:

Start Progres database with docker (docker preinstallation required)
docker-compose up -d

Migrate database schema:
python manage.py makemigrations
python manage.py migrate

Import data from csv file
python import-data.py

Create a super user
python manage.py createsuperuser

Run backend server
python manage.py runserver 8100

From browser login with super user account. You should be all set to have an initial play. 

Have fun!
