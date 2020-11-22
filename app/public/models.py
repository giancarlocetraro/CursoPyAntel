# app/public/models.py

# importamos la instancia de la BD
from app import db

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(64), index=True, unique=True)
    preguntas = db.relationship('Pregunta', backref='categoria', lazy='dynamic')

    def __repr__(self):
        return f'<Categoria: {self.descripcion}>'


class Pregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False, unique=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    respuestas = db.relationship('Respuesta', backref='pregunta', lazy='dynamic')

    def __repr__(self):
        return f'<Pregunta: {self.text}>'


class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False, unique=True)
    valid = db.Column(db.Boolean, nullable=False, default=False)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('pregunta.id'))

    def __repr__(self):
        return f'<Respuesta: {self.text}>'


class Posiciones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    time = db.Column(db.Interval, nullable=False)

    def __repr__(self):
        return '<Usuario: {} - Time: {}>'.format(self.name, self.time)
