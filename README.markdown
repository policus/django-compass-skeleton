# Overview

Provides a simple structure for Django and Compass projects

# Usage

First, clone the skeleton to a new directory

	git clone git@github.com:policus/django-compass-skeletion.git YOUR_PROJECT

Change the name of your project directory to match your project

	cd YOUR_PROJECT
	mv django-compass-skeleton YOUR_PROJECT

Customize files for your project. In particular:

	YOUR_PROJECT/conf/common.py - SECRET_KEY and ROOT_URLCONF
	YOUR_PROJECT/conf/development.py - DATABASES
	YOUR_PROJECT/deploy/gunicorn.conf.py

Install requirements

	mkvirtualenv YOUR_PROJECT
	pip install -r requirements.txt
