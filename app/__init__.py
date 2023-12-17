from logging.handlers import RotatingFileHandler
import logging
import os

from flask import Flask
app = Flask(__name__)
from app import routes

# from app.api import bp as api_bp
# app.register_blueprint(api_bp, url_prefix='/api')

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/fs-api.log', maxBytes=10240000,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('fs-api start')