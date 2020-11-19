# app/errors/routes.py

from . import errors_bp
from flask import render_template, jsonify
from werkzeug.exceptions import HTTPException


@errors_bp.app_errorhandler(401)
def unathorized(e):
    #return jsonify(error=str(e)), 401
    return render_template('401.html'), 401


@errors_bp.app_errorhandler(403)
def page_not_found(e):
    # return jsonify(error=str(e)), 403
    return render_template('403.html'), 403


@errors_bp.app_errorhandler(404)
def page_not_found(e):
    # return jsonify(error=str(e)), 404
    return render_template('404.html'), 404


@errors_bp.app_errorhandler(HTTPException)
def handle_exception(e):
    #return jsonify(error=str(e)), e.code
    return render_template('500.html', msj=str(e)), 500
