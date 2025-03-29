import os
from flask import Flask
from flasgger import Swagger
from .routes.routes import main as main_blueprint
from .extensions import db, migrate
from flask_cors import CORS

from .messages.errors.handlers import configure_error_handlers
from .logs.logger import configure_logging
from .config.config import config

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    env = os.getenv('FLASK_ENV', 'development')
    configure_error_handlers(app)
    app.config.from_object(config[env])
    configure_logging(app)
    
    # Inicializa o Flasgger APENAS se estiver habilitado
    if app.config.get('SWAGGER', {}).get('enabled', False):
        Swagger(app, template=app.config['SWAGGER'])
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Registro das rotas
    app.register_blueprint(main_blueprint)
    
    return app