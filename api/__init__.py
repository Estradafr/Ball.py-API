import os

from flask import Flask, redirect
from flask_migrate import Migrate
from dotenv import load_dotenv

psql_connection_string = os.getenv("psql_connection_string")

def create_app():
    
    # factory 
    app = Flask(__name__)
    
    # db config
    app.config['SQLALCHEMY_DATABASE_URI'] = psql_connection_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    
    # index route
    @app.route('/')
    def index():
        return redirect('/reptiles')
    
    # registerring the bluep
    from . import reptile
    app.register_blueprint(reptile.bp)
    
    return app        
