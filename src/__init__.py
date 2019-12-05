from flask import Flask
import connexion
import os
from logbook import Logger , StreamHandler , ERROR, WARNING, DEBUG, INFO
import sys
from config import Devconfig , Prodconfig   , Testconfig
from environs import Env

### Setting environement configuration depending on environement variable
env = Env()
if env('FLASK_ENV', 'developement') == 'developement':
	DefaultConfig = Devconfig
elif env('FLASK_APP') == 'production':
	DefaultConfig = Prodconfig 
else :
	DefaultConfig = Testconfig

def create_app(config_class = DefaultConfig):
	app = connexion.FlaskApp(
		    __name__, specification_dir='openapi/', options={"swagger_ui": False, "serve_spec": False}
		)
	app.app.config.from_object(config_class)

	log = Logger('logbook')
	log.info(app.app.config['LOG_LEVEL'])
	#show logging messages in terminal
	StreamHandler(sys.stdout ,
		level = app.app.config['LOG_LEVEL']).push_application()

	log.info('welcome to my application API MODE {}'.format(env('FLASK_ENV','developement')))

	app.add_api("swagger.yml", strict_validation=True)
	log.info('I ADDED SWAGGER YAML')
	flask_app = app.app
	return flask_app




