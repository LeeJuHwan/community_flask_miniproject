from flask import Blueprint, render_template, redirect, url_for,g, request
from ..db import conn, cur
from ..form import AnswerForm, QuestionForm
from datetime import datetime
bp = Blueprint('board', __name__, url_prefix='/board')


@bp.route("/")
def select() :
    sql="""
    SELECT b.id, username, b.title, b.content, b.write_date, t.lang, b.views,
    ifnull((select count(*) from reply r where b.id = r.board_id), 0) as cnt_reply,
    (select count(*) from board) as cnt_board
    from board b join user u on b.user_id = u.id join tag t on t.id = b.tag_id;
    """
    cur.execute(sql)
    data_list = cur.fetchall()
    # print("select data list", data_list)
    # if data_list is None :
    #     data_list.append({'cnt_reply' : 0})
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
    print(reply)
    print("reply sql 유효 검사", type(reply), reply) # tuple 
    print("reply board id값 검사", board_id)
    if len(reply) == 0 :
        return render_template("detail.html", board = board, reply = [{'cnt' : 0}], form = form)
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
    print("********",board)
    cur.execute(sql)
    reply = cur.fetchall()
    return render_template('detail.html', board=board, form=form, reply=reply)
    


@bp.route("users")
def show_users() :
    return render_template("users.html")

@bp.route("write", methods = ("POST","GET"))
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
    print("equest.method 검사 233",request.method)


    if request.method == "POST" :
        print("####", request.form["language"])
        tag_select = request.form["language"]
        sql = f"""
        select t.id from tag t left outer join board b on t.id = b.tag_id 
        where lang = '{tag_select}';
        """
        cur.execute(sql)
        select_tag_id = cur.fetchall()[0]
        print("포스트 id 값 조회", select_tag_id)
        print(form.title.data, form.content.data, datetime.now())
        sql = f"""
          insert into board (title, content, write_date, user_id, tag_id) values ('{form.title.data}','{form.content.data}','{datetime.now()}', {g.user['user_id']}, {select_tag_id['id']})
         """
         
        cur.execute(sql)
        conn.commit()
        print("commit 후 검사 #########")
        return redirect(url_for('board.select', tag_list = tag_list, form = form))

    
    return render_template('write.html', form=form, tag_list=tag_list)

@bp.route("test3")
def test3() :
    return render_template("mypage.html")

@bp.route("grade")
def grade() :
    return render_template("grade.html)