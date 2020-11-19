#!/usr/bin/env python
# -*- coding: utf-8 -*-

# importamos la instancia de la BD
from app import db

from flask import Flask
from app.public.models import Categoria, Pregunta, Respuesta
from app.auth.models import Usuario, Rol


app = Flask(__name__)
POSTGRES = {
    'user': 'postgres',
    'pw': 'admin',
    'db': 'trivia',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()

    # categorias
    c_geogra = Categoria(descripcion="Geografía")
    c_deporte = Categoria(descripcion="Deportes")
    c_historia = Categoria(descripcion="Historia")
    c_arte = Categoria(descripcion="Arte")

    # preguntas
    q_Laos = Pregunta(text="¿Cuál es la capital de Laos?", categoria=c_geogra)
    q_Armenia = Pregunta(text="¿Cuál es la población aproximada de Armenia?", categoria=c_geogra)
    q_mundial = Pregunta(text="¿En qué país se jugó la Copa del Mundo de 1962?", categoria=c_deporte)
    q_formula = Pregunta(text="¿Con qué equipo debutó Sebastian Vettel en Formula 1?", categoria=c_deporte)
    q_napo = Pregunta(text="¿En que isla murió Napoleón?", categoria=c_historia)
    q_colon = Pregunta(text="¿En que año descubrió Colón América?", categoria=c_historia)
    q_mona = Pregunta(text="¿En que museo está la Mona Lisa?", categoria=c_arte)
    q_pica = Pregunta(text="¿En que año pinto Picasso el Guernica?", categoria=c_arte)

    # respuestas
    a_Laos_a = Respuesta(text="Nom Pen", valid=False, pregunta=q_Laos)
    a_Laos_b = Respuesta(text="Vientián", valid=True, pregunta=q_Laos)
    a_Laos_c = Respuesta(text="Hanói", valid=False, pregunta=q_Laos)
    a_Armenia_a = Respuesta(text="3 millones", valid=True, pregunta=q_Armenia)
    a_Armenia_b = Respuesta(text="2 millones", valid=False, pregunta=q_Armenia)
    a_Armenia_c = Respuesta(text="9 millones", valid=False, pregunta=q_Armenia)
    a_mundial_a = Respuesta(text="México", valid=False, pregunta=q_mundial)
    a_mundial_b = Respuesta(text="Argentina", valid=False, pregunta=q_mundial)
    a_mundial_c = Respuesta(text="Chile", valid=True, pregunta=q_mundial)
    a_formula_a = Respuesta(text="Red Bull", valid=False, pregunta=q_formula)
    a_formula_b = Respuesta(text="Ferrari", valid=False, pregunta=q_formula)
    a_formula_c = Respuesta(text="BMW Sauber", valid=True, pregunta=q_formula)
    a_napo_a = Respuesta(text="Santa Elena", valid=True, pregunta=q_napo)
    a_napo_b = Respuesta(text="Corcega", valid=False, pregunta=q_napo)
    a_napo_c = Respuesta(text="Elba", valid=False, pregunta=q_napo)
    a_colon_a = Respuesta(text="1496", valid=False, pregunta=q_colon)
    a_colon_b = Respuesta(text="1492", valid=True, pregunta=q_colon)
    a_colon_c = Respuesta(text="1488", valid=False, pregunta=q_colon)
    a_mona_a = Respuesta(text="Museo del Prado", valid=False, pregunta=q_mona)
    a_mona_b = Respuesta(text="Galería Uffizi", valid=False, pregunta=q_mona)
    a_mona_c = Respuesta(text="Louvre", valid=True, pregunta=q_mona)
    a_pica_a = Respuesta(text="1937", valid=True, pregunta=q_pica)
    a_pica_b = Respuesta(text="1947", valid=False, pregunta=q_pica)
    a_pica_c = Respuesta(text="1957", valid=False, pregunta=q_pica)

    # Usuarios
    user1 = Usuario(name="giancarlo", email="gcetraro@gmail.com")
    user1.set_password("1234")

    # usuario administrador
    admin1 = Usuario(name="admin", email="admin@blabla.com")
    admin1.set_password("admin1")

    # roles
    rolA = Rol(rolename='admin', usuario=admin1)
    rolU = Rol(rolename='user', usuario=user1)

    db.session.add(c_geogra)
    db.session.add(c_historia)
    db.session.add(c_arte)
    db.session.add(c_deporte)

    db.session.add(q_Laos)
    db.session.add(q_Armenia)
    db.session.add(q_napo)
    db.session.add(q_colon)
    db.session.add(q_mona)
    db.session.add(q_pica)
    db.session.add(q_mundial)
    db.session.add(q_formula)

    db.session.add(a_Laos_a)
    db.session.add(a_Laos_b)
    db.session.add(a_Laos_c)
    db.session.add(a_Armenia_a)
    db.session.add(a_Armenia_b)
    db.session.add(a_Armenia_c)
    db.session.add(a_mundial_a)
    db.session.add(a_mundial_b)
    db.session.add(a_mundial_c)
    db.session.add(a_formula_a)
    db.session.add(a_formula_b)
    db.session.add(a_formula_c)
    db.session.add(a_napo_a)
    db.session.add(a_napo_b)
    db.session.add(a_napo_c)
    db.session.add(a_colon_a)
    db.session.add(a_colon_b)
    db.session.add(a_colon_c)

    db.session.add(user1)
    db.session.add(admin1)

    db.session.add(rolA)
    db.session.add(rolU)

    db.session.commit()

    # recorremos categorias y sus preguntas
    categorias = Categoria.query.all()
    for c in categorias:
        print(c.id, c.descripcion)
        # para cada categoria, obtenemos sus preguntas y las recorremos
        for p in c.preguntas:
            print(p.id, p.text)

    usuarios = Usuario.query.all()
    for u in usuarios:
        print(u.id, u.name)
        for r in u.roles:
            print(r.id, r.rolename)

    #cat = Categoria.query.get(1)
    #print(cat)
print("Populate done!")
