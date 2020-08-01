import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None):
    # creating and configuring the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'devel',
        DATABASE=os.path.join(app.instance_path, 'forms.sqlite'),
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:\\\db.db'


    from models import db

    
    db.init_app(app)

    if test_config is None:
        # load the instance config when not testing and if exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return 'the first fucking page'
    
    return app