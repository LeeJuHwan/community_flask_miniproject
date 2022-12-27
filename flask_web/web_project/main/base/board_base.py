from flask import Blueprint, render_template, redirect, url_for,g, request
from ..db import conn, cur
from ..form import AnswerForm, QuestionForm
from datetime import datetime
bp = Blueprint('board', __name__, url_prefix='/board')


@bp.route("/")
def select() :
    sql="""
    SELECT b.id, username, b.title, b.content, b.write_date, t.lang, b.views,
    (select count(*) from reply r where b.id = r.board_id) as cnt_reply,
    (select count(*) from board) as cnt_board
    from board b join user u on b.user_id = u.id join tag t on t.id = b.tag_id;
    """
    cur.execute(sql)
    data_list = cur.fetchall()
    print("select data list", data_list)
    return render_template("test/test.html", data_list = data_list)

@bp.route("detail/<int:board_id>")
def detail(board_id) : 
    form = AnswerForm()
    sql = f"""
    select b.*, username from board b join user u on b.user_id = u.id
    where b.id = {board_id}
    """
    cur.execute(sql)
    board = cur.fetchone()
    print("detail sql 유효 검사", board)
    print("board id값 검사", board_id)
    

    sql = f"""
    select *, (select count(*) from reply where board_id = {board_id} ) as cnt, b.id from reply r join board b on r.board_id = b.id
    where r.board_id = {board_id};
    """
    cur.execute(sql)
    reply = cur.fetchall()
    print("reply sql 유효 검사", reply)
    print("reply board id값 검사", board_id)
    
    return render_template("detail.html", board = board, reply = reply, form = form)

@bp.route("answer/<int:board_id>", methods = ('POST',))
def reply_create(board_id):
    if g.user is None :
        return redirect(url_for('user.login'))
    form = AnswerForm()
    print("입력방식 검사", form.validate_on_submit())
    if form.validate_on_submit():
        content = request.form["content"]
        sql = f"""
        INSERT INTO reply (board_id, content, reply_date, user_id)
        VALUES ({board_id},'{content}','{datetime.now()}',{g.user['user_id']})
        """
        cur.execute(sql)
        conn.commit()
        print("board id test", board_id)
        return redirect(url_for("board.detail", board_id = board_id))

    sql  = f"""
    SELECT * FROM board WHERE id = {board_id}
    """
    cur.execute(sql)
    board = cur.fetchone()
    sql = f"""
    SELECT * FROM reply WHERE board_id = {board_id}
    """
    cur.execute(sql)
    reply = cur.fetchall()
    return render_template('detail.html', board=board, form=form, reply=reply)


@bp.route("users")
def show_users() :
    return render_template("users.html")
    
@bp.route("write", methods = ("GET", "POST"))
def board_write() :
    if g.user is None :
        return redirect(url_for('user.login'))
    form = QuestionForm()
    sql = f"""
    select lang from tag;
    """
    cur.execute(sql)
    tag_list = cur.fetchall()
    print("sql 출력물 검사", tag_list)
    # if request.method == "POST" and form.validate_on_submit():
    #     sql = f"""
    #     insert into board(user_id, title, content, write_date,tag_id) values (2, '게시글2', '테스트2', '2022-12-26', 2);
    #     insert into board (title, content, create_date, user_id) values ('{form.subject.data}','{form.content.data}','{datetime.now()}', {g.user['user_id']})
    #     """
    #     cur.execute(sql)
    #     conn.commit()
    #     return redirect(url_for('board.select'))
    return render_template("write.html", tag_list = tag_list, form = form)

def tag_select() :
    sql = """
    select lang from tag
    """
    cur.execute(sql)
    tag_list = cur.fetchall()
    return render_template("ssen.html", tag_list = tag_list)




@bp.route("test3")
def test3() :
    return render_template("mypage.html")

