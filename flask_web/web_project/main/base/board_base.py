from flask import Blueprint, render_template, redirect, url_for

bp = Blueprint('board', __name__, url_prefix='/board')

@bp.route("/")
def select() :
    return render_template("board.html")

@bp.route("/test")
def test() :
    return render_template("jiye.html")