from flask import Blueprint, render_template, redirect, url_for
from ..db import conn, cur

bp = Blueprint("main", __name__, url_prefix="/")

@bp.route("/")
def index() :
    return render_template("index.html")

@bp.route("/users")
def users() :
    return render_template("users.html")

@bp.route("/mypage")
def mp() :
    return render_template("mypage.html")