"""
Backend for login page
"""

from flask import flash
from flask import request
from flask import Blueprint
from flask import render_template


bp = Blueprint("login", __name__)


@bp.route("/")
def index():
    flash("Log in to the scrum management app")
    return render_template("login.html")


@bp.route("/login", methods=['POST', 'GET'])
def login():
    flash(f"You are login as: {str(request.form['name_input'])}")
    return render_template("login.html")
