import os

from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    # creating and configuring the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'devel-fapsco',
        DATABASE=os.path.join(app.instance_path, 'forms.sqlite'),
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/uploads')
    app.config['ALLOWED_EXTESIONS'] =['jpg', 'png', 'jpeg', 'pdf', 'docx']
    app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024;

    db.init_app(app)
    migrate.init_app(app, db)

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

    @app.route('/about')
    def about():
        return render_template('about.html')


    from .views.electronics import bp


    app.register_blueprint(bp)
    app.add_url_rule('/', 'index')
    
    return app