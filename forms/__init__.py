import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app(test_config=None):
    # creating and configuring the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'devel-fapsco',
        DATABASE=os.path.join(app.instance_path, 'forms.sqlite'),
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'


    from .models import db, migrate

    
    db.init_app(app)
    migrate.init_app(app, db)


    from .views.electronics import bp


    app.register_blueprint(bp)
    app.add_url_rule('/', 'index')

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
    
    return app