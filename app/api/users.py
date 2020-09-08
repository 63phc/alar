from flask import render_template

from flask_login import current_user

from . import bp
from app.db.models import User


@bp.route("/", methods=("GET",))
def index():
    if not current_user.is_active:
        return render_template("login.html")
    else:
        users = User.query.all()
        return render_template("users_list.html", users=users, user=current_user)
