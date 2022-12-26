from flask import Blueprint, render_template, redirect, url_for
from ..db import conn, cur


bp = Blueprint('board', __name__, url_prefix='/board')

@bp.route("/")
def select() :
    return render_template("board.html")

@bp.route("test")
def test() :
    sql="""
    SELECT username, b.title, b.content, b.write_date, t.lang, b.views,
    (select count(*) from reply r where b.id = r.board_id) as cnt_reply from board b join user u on b.user_id = u.id join tag t on t.id = b.tag_id;
    """
    cur.execute(sql)
    data_list = cur.fetchall()
    print(data_list)
    return render_template("test/test.html", data_list = data_list)