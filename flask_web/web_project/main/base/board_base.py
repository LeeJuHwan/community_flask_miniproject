from flask import Blueprint, render_template, redirect, url_for,g, request, flash
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
    from board b join user u on b.user_id = u.id join tag t on t.id = b.tag_id order by b.id desc;
    """
    cur.execute(sql)
    data_list = cur.fetchall()
    # print("select data list", data_list)
    # if data_list is None :
    #     data_list.append({'cnt_reply' : 0})
    return render_template("test/test.html", data_list = data_list)

@bp.route("detail/<int:board_id>", methods = ["GET", "POST"])
def detail(board_id) : 
    form = AnswerForm()
    sql = f"""
    select b.*, username from board b join user u on b.user_id = u.id
    where b.id = {board_id};
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


## --> 답변 등록 폼 
########################################################
    if request.method == 'POST':
        content = request.form["content"]
        sql = f"""
        INSERT INTO reply (board_id, content, reply_date, user_id)
        VALUES ({board_id},'{content}','{datetime.now()}',{g.user['user_id']})
        """
        cur.execute(sql)

        conn.commit()
        
        return redirect(url_for("board.detail", board_id = board_id))
################################################################
    sql = f"""
    select count(*) as cnt from reply where board_id={board_id}
    """
    cur.execute(sql)
    cnt_reply = cur.fetchone()['cnt']
    
    print("###########", type(reply))
    print(reply)
    if len(reply) == 0 :
        return render_template("detail.html", board = board, reply = reply, cnt_reply = cnt_reply, form = form)
    return render_template("detail.html", board = board, reply = reply, cnt_reply = cnt_reply,  form = form)


## --> 라우팅 함수 액션 후 반응 없음(주석 처리 후, 디테일 함수에서 수정)
# @bp.route("answer/<int:board_id>", methods = ['POST',])
# def reply_create(board_id):
#     if g.user is None :
#         return redirect(url_for('user.login'))
#     form = AnswerForm()
#     print("입력방식 검사", form.validate_on_submit())
#     if form.validate_on_submit():
#         content = request.form["content"]
#         sql = f"""
#         INSERT INTO reply (board_id, content, reply_date, user_id)
#         VALUES ({board_id},'{content}','{datetime.now()}',{g.user['user_id']})
#         """
#         cur.execute(sql)
#         conn.commit()
#         print("board id test", board_id)
#         return redirect(url_for("board.detail", board_id = board_id))

#     sql  = f"""
#     SELECT * FROM board WHERE id = {board_id}
#     """
#     cur.execute(sql)
#     board = cur.fetchone()
#     print(board, "에러 확인")
#     sql = f"""
#     SELECT * FROM reply WHERE board_id = {board_id}
#     """
    
#     cur.execute(sql)
#     reply = cur.fetchall()
#     print("********",reply)
#     return render_template('detail.html', board=board, form=form, reply=reply)
    

@bp.route('/delboard/<int:board_id>')
def delboard(board_id):
    sql = f'''delete from board where id={board_id}'''
    cur.execute(sql)
    conn.commit()
    
    return redirect(url_for('board.select'))


@bp.route('/delreply/<int:board_id>/<int:reply_id>')
def delreply(board_id, reply_id):
    sql = f'''delete from reply where id={reply_id}'''
    cur.execute(sql)
    conn.commit()
    
    return redirect(url_for('board.detail', board_id=board_id))

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
        
        return redirect(url_for('board.select', tag_list = tag_list, form = form))

    
    return render_template('write.html', form=form, tag_list=tag_list)


@bp.route('/open_modify/<int:board_id>', methods=('POST','GET'))
def board_modify(board_id):
    sql = f"select * from board where id={board_id}"
    cur.execute(sql)
    board = cur.fetchall()[0]

    sql = f"""
    select lang from tag;
    """
    cur.execute(sql)
    tag_list = cur.fetchall()

    print("modify", board)
    print("tag", tag_list)

    if g.user['user_id'] != board['user_id']:
        flash('수정권한이 없습니다')
        return redirect(url_for('board.detail', board_id=board_id))

    if request.method == 'POST':  # POST 요청
        form = QuestionForm()
        tag_select = request.form["language"]
        sql = f"""
        select t.id from tag t left outer join board b on t.id = b.tag_id 
        where lang = '{tag_select}';
        """
        cur.execute(sql)
        select_tag_id = cur.fetchall()[0]

        if form.validate_on_submit():
            sql = f"update board set title='{form.title.data}', content='{form.content.data}', modify_date='{datetime.now()}', tag_id = {select_tag_id['id']} where id={board_id};"
            cur.execute(sql)
            conn.commit()
        
            return redirect(url_for('board.detail', board_id=board_id))
        # else:
        #     return redirect(url_for('board.detail', board_id=board_id))
        
    else:  # GET 요청
        form = QuestionForm(title=board['title'], content=board['content'])
        return render_template('write.html', form=form, tag_list = tag_list)




######################################################################
@bp.route('/reply_modify/<int:board_id>/<int:reply_id>', methods=('POST','GET'))
def reply_modify(reply_id, board_id) : 
    
    print("#" * 25,reply_id)
    print("#" * 25,board_id)

    sql = f"select * from board where id={board_id}"
    cur.execute(sql)
    board = cur.fetchall()[0]

    sql = f"select * from reply where id={reply_id}"
    cur.execute(sql)
    reply = cur.fetchall()[0]

    print(reply)
    if g.user['user_id'] != reply['user_id']:
        flash('수정권한이 없습니다')
        return redirect(url_for('board.detail', reply_id=reply.board_id))

    if request.method == 'POST':  # POST 요청
        form = AnswerForm()
        if form.validate_on_submit():
            sql = f"""update reply set content='{form.content.data}', modify_date='{datetime.now()}' 
            where id={reply_id};"""
            cur.execute(sql)
            conn.commit()
            return redirect(url_for('board.detail', board_id=reply['board_id']))
    else:
        form = AnswerForm(content=reply['content'])

    sql = f"""
    select b.*, username from board b join user u on b.user_id = u.id
    where b.id = {board_id};
    """
    cur.execute(sql)
    board = cur.fetchone()

    sql = f"""
    select *, (select count(*) from reply where board_id = {board_id} ) as cnt, b.id from reply r join board b on r.board_id = b.id
    where r.board_id = {board_id};
    """
    cur.execute(sql)
    reply = cur.fetchall()
    print("reply test", reply)

    if len(reply) == 0 :
        return render_template("detail.html", board = board, reply = [{'cnt' : 0}], form = form)

    return render_template('detail.html', form=form, reply = reply, board = board)


@bp.route("tags")
def tags() :
    return render_template("tags.html")

@bp.route("grade")
def grade() :
    return render_template("grade.html")






# @bp.route("question/<int:board_id>")
# def question(board_id) : 
#     form = AnswerForm()
#     sql = f"""
#     select b.*, username from board b join user u on b.user_id = u.id
#     where b.id = {board_id}
#     """
#     cur.execute(sql)
#     board = cur.fetchone()
#     print("detail sql 유효 검사", board)
#     print("board id값 검사", board_id)
    

#     sql = f"""
#     select *, (select count(*) from reply where board_id = {board_id} ) as cnt, b.id from reply r join board b on r.board_id = b.id
#     where r.board_id = {board_id};
#     """
#     cur.execute(sql)
#     reply = cur.fetchall()
#     print("reply sql 유효 검사", reply)
#     print("reply board id값 검사", board_id)
    
#     return render_template("detail.html", board = board, reply = reply, form = form)

# @bp.route("answer/<int:board_id>", methods = ('POST',))
# def reply_upload(board_id):
#     if g.user is None :
#         return redirect(url_for('user.login'))
#     form = AnswerForm()
#     print("입력방식 검사", form.validate_on_submit())
#     if form.validate_on_submit():
#         content = request.form["content"]
#         sql = f"""
#         INSERT INTO reply (board_id, content, reply_date, user_id)
#         VALUES ({board_id},'{content}','{datetime.now()}',{g.user['user_id']})
#         """
#         cur.execute(sql)
#         conn.commit()
#         print("board id test", board_id)
#         return redirect(url_for("board.detail", board_id = board_id))

# @bp.route('/modify/<int:answer_id>', methods=('GET', 'POST'))
# def reply_modify(reply_id):
#     sql = f"""
#     SELECT * FROM reply WHERE id = {reply_id}"
#     """
#     cur.execute(sql)
#     reply = cur.fetchone()
#     if g.user['user_id'] != reply['user_id']:
#         flash('수정권한이 없습니다')
#         return redirect(url_for('board.detail', question_id=reply.id))
#     if request.method == "POST":
#         form = AnswerForm()
#         if form.validate_on_submit():
#             sql = f"update answer set content='{form.content.data}', modify_date='{datetime.now()}' where id={reply_id};"
#             cur.execute(sql)
#             conn.commit()
#             return redirect(url_for('board.detail', reply_id=reply['id']))
#     else:
#         form = AnswerForm(content=reply['content'])
#     return render_template('detail.html', form=form)

# @bp.route('/modify/<int:question_id>', methods=('GET', 'POST'))
# def board_modify(board_id):
#     sql = f"select * from question where id={board_id}"
#     cur.execute(sql)
#     board = cur.fetchall()[0]

#     if g.user['user_id'] != question['user_id']:
#         flash('수정권한이 없습니다')
#         return redirect(url_for('board.detail', board_id=board_id))

#     if request.method == 'POST':  # POST 요청
#         form = QuestionForm()
#         tag_select = request.form["language"]
#         sql = f"""
#         select t.id from tag t left outer join board b on t.id = b.tag_id 
#         where lang = '{tag_select}';
#         """
#         cur.execute(sql)
#         select_tag_id = cur.fetchall()[0]

#         if form.validate_on_submit():
#             sql = f"update board set title='{form.title.data}', content='{form.content.data}', modify_date='{datetime.now()}', tag_id = {select_tag_id} where id={board_id};"
#             print("if sql", sql)
#             cur.execute(sql)
#             conn.commit()
            
#             return redirect(url_for('question.detail', board_id=board_id))
        
#     else:  # GET 요청
#         form = QuestionForm(title=board['title'], content=board['content'])
#         return render_template('wrtie.html', form=form)