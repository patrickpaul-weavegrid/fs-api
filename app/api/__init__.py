from flask import Blueprint
bp = Blueprint('api', __name__)
from app.api import fs_resource
