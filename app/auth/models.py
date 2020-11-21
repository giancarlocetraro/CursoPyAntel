# app/auth/models.py

# importamos la instancia de la BD
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from sqlalchemy.sql import func

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    register_date = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    roles = db.relationship('Rol', backref='usuario', lazy='dynamic')

    def __repr__(self):
        return '<Usuario: {} - Email: {}>'.format(self.name, self.email)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_admin(self):
        return self.is_admin

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def get_by_email(email):
        return Usuario.query.filter_by(email=email).first()


class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(60), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    def __repr__(self):
        return f'<Rol: {self.rolename}>'
