from flask import Blueprint, render_template, redirect, url_for
from ..db import conn, cur

bp = Blueprint("main", __name__, url_prefix="/")

@bp.route("/")
def index() :
    return render_template("index.html")