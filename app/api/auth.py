from flask import url_for

from flask_login import login_required, logout_user
from werkzeug.utils import redirect

from . import bp
from app.service.auth import user_login


@bp.route("/login", methods=["POST"])
def login():
    return user_login()


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("/.index"))
