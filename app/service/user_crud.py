import sqlalchemy
from flask import render_template, url_for, request, flash
from flask_login import current_user
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from app import db
from app.db.models import User, Role
from app.forms import CreateUserForm


def user_create():
    """FIXME: создания юзера через форму с flask-wtf, юзал первый раз, надеюсь последний"""
    form = CreateUserForm()
    if form.validate_on_submit():
        email = form.email.data
        role = form.role_id.data
        password = generate_password_hash(form.password.data, method="sha256")
        try:
            new_user = User(email=email, role_id=role, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("/.index"))
        except sqlalchemy.exc.SQLAlchemyError:
            db.session.rollback()
            flash("User allready exist")
    db.session.close()
    return render_template("user_edit.html", user=current_user, form=form)


def user_edit(action: str, id: int):
    """FIXME: Хотел зарефаторить и вынести удаление в другой метод и поинт уже с AJAX - но руки не дошли"""
    if not current_user.is_moderator:
        return redirect(url_for("/.index"))

    query_user = db.session.query(User).filter(User.id == id)
    user = query_user.one_or_none()

    if request.method == "POST" and action == "edit":
        email = request.form.get("email") or user.email or None
        role = request.form.get("role") or 1
        if email:
            query_user.update(dict(email=email, role_id=int(role)))
            db.session.commit()
            return redirect(url_for("/.index"))

    if action == "delete":
        db.session.execute(f"delete from public.user where id = {id};")
        db.session.commit()
        flash("Entry deleted")
        # logout_user(user)
        return redirect(url_for("/.index"))

    role = db.session.query(Role).filter(Role.title != user.role.title).all()
    return render_template("user_edit.html", user=user, role=role)
