from flask import request, flash, url_for
from flask_login import login_user
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect

from ..db.models import User


def user_login():
    """FIXME: логин юзера, валидация только на клиенте"""
    email = request.form.get("email")
    password = request.form.get("password")
    remember = request.form.get("remember") or False

    user = User.query.filter_by(email=email).first()

    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again.")
        return redirect(url_for("/.index"))

    login_user(user, remember=remember)
    return redirect(url_for("/.index"))
