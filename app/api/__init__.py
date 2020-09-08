from flask import Blueprint

bp = Blueprint("/", __name__)

from .auth import *
from .user_crud import *
from .users import *
from .data_points import *
