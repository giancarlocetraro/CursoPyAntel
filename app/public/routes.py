# app/public/routes.py

from app import login_required, db
from flask import render_template, session
from flask_login import current_user
from . import public_bp
from .models import Categoria, Pregunta, Respuesta, Posiciones
import random
from datetime import datetime

@public_bp.route('/trivia')
def index():
    # abort(400)
    return render_template('index.html')


@public_bp.route('/trivia/categorias', methods=['GET'])
@login_required
def mostrarcategorias():
    categorias = Categoria.query.all()

    # seteo tiempo inicial y diccionario de categorias con las claves en false
    if 'init_time' not in session.keys():
        session['init_time'] = datetime.now()
        for cat in categorias:
            session[str(cat.id)] = False

    return render_template('categorias.html', categorias=categorias)


@public_bp.route('/trivia/<int:id_categoria>/pregunta', methods=['GET'])
@login_required
def mostrarpregunta(id_categoria):
    preguntas = Pregunta.query.filter_by(categoria_id=id_categoria).all()
    categ = Categoria.query.get(id_categoria)
    # elegir pregunta aleatoria pero de la categoria adecuada
    pregunta = random.choice(preguntas)
    respuestas = pregunta.respuestas

    return render_template('preguntas.html', categoria=categ, pregunta=pregunta, respuestas=respuestas)


@public_bp.route('/trivia/<int:id_categoria>/<int:id_pregunta>/respuesta/<int:id_respuesta>', methods=['GET'])
@login_required
def mostrarresultado(id_categoria, id_pregunta, id_respuesta):
    cats = Categoria.query.all()
    pregunta = Pregunta.query.get(id_pregunta)
    respuesta = Respuesta.query.get(id_respuesta)

    if respuesta.valid:
        result = 'Correcta!'
        session[str(id_categoria)] = True

        # verifico si se llegó al final del juego (todas las categorias satisfechas)
        fin = True
        for c in cats:
            if session[str(c.id)] == False:
                fin = False
                break

        if fin:
            session['total_time'] = datetime.now() - session['init_time']
            pos = Posiciones(name=current_user.name, time=session['total_time'])
            db.session.add(pos)
            db.session.commit()
            print(pos)
            #print(type(session['total_time']))
            tiempo = str(session['total_time'])
            #sec = session['total_time'].total_seconds()
            #print(sec)
            #tiempo = '%H:%M:%S'.format(sec // 3600, sec % 3600 // 60, sec % 60)
            top_cinco = Posiciones.query.order_by(Posiciones.time).limit(5)
            session.clear()
            return render_template('fin.html', tiempo=tiempo, tabla=top_cinco)
    else:
        result = 'Incorrecta'

    return render_template('resultado.html', pregunta=pregunta, resultado=result)
