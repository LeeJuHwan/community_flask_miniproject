from flask import Blueprint, render_template, url_for, redirect, request

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route("/")
def log():
    return render_template("login.html")