from flask import Blueprint, render_template, redirect, url_for
from ..db import conn, cur


bp = Blueprint('board', __name__, url_prefix='/board')

@bp.route("/")
def select() :
    return render_template("board.html")

@bp.route("/questions")
def questions() :
    sql="""
    SELECT username, b.title, b.content, b.write_date, t.lang, b.views,
    (select count(*) from reply r where b.id = r.board_id) as cnt_reply from board b join user u on b.user_id = u.id join tag t on t.id = b.tag_id;
    """
    cur.execute(sql)
    data_list = cur.fetchall()
    print(data_list)
    return render_template("questions.html", data_list = data_list)

@bp.route("/details")
def details():
    return render_template("details.html")

@bp.route("/users")
def users():
    return render_template("users.html")

@bp.route("/nav")
def nav() :
    return render_template("board_yj.html")


@bp.route("/faq")
def faq() :
    sql = 'SELECT * FROM board;'
    cur.execute(sql)
    qna_list = cur.fetchall()
    return render_template("FAQ.html",qna_list=qna_list)

@bp.route("/qna")
def qna():
    sql = 'SELECT * FROM board;'
    cur.execute(sql)
    board_list = cur.fetchall()
    
    return render_template("QNA.html", board_list=board_list)
