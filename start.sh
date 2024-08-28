#! /bin/sh

python gamestonks/manage.py makemigrations

python gamestonks/manage.py migrate

python gamestonks/manage.py runserver
