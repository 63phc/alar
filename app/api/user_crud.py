from flask_login import login_required

from app.service.user_crud import user_create, user_edit
from app.api import bp


@bp.route("/user/<action>/<id>", methods=("GET", "POST"))
@login_required
def user_crud(action, id):
    return user_edit(action, id)


@bp.route("/user/add/new", methods=("POST", "GET"))
def create():
    return user_create()
