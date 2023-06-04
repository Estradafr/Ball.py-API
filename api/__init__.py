import os

from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv

psql_connection_string = os.getenv("psql_connection_string")

def create_app():
    
    # factory 
    app = Flask('App')
    
    # db config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False     
    
    # index route
    @app.route('/')
    def index():
        return 'Index page'
    
    return app        
