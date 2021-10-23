#!/bin/bash

#source ./env/bin/activate

#This command tell flask to look for apps in "app" folder
export FLASK_APP=app

#This command to identify that application shall be run in "development" mode which tell server to automatically restart if any modifications is applied on app file
#

#    development: a development environment that generally uses for local development environments

#    product: production environments for online deployment

#    testing: for test environments, general for various test uses

export FLASK_ENV=development

#run app directly but you must cd to parent of 'flaskr' folder which is 'part2' folder
flask run

#curl http://127.0.0.1:5000/plants
