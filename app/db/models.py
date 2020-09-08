from datetime import datetime

from flask_login import UserMixin
from sqlalchemy.orm import relationship

from . import db


class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)

    def __str__(self):
        return self.title


class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    role = relationship(Role, backref="role")

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=True)

    def __repr__(self):
        return f"<User login: {self.email}>"

    @property
    def is_moderator(self):
        return True if self.role.title == "Moderator" else False
