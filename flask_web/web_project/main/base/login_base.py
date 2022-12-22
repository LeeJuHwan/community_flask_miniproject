from flask import Blueprint, url_for, render_template, flash, request, session, g, redirect
from ..form import UserCreateForm, UserLoginForm
from ..db import conn, cur
from werkzeug.security import generate_password_hash, check_password_hash

# 블루프린트 생성
bp = Blueprint('user', __name__, url_prefix='/user')

# 회원가입 
@bp.route('/register/', methods=('GET', 'POST'))
def register():
    form = UserCreateForm()
    print("form", form)
        # --> 회원가입 버튼을 눌렀을 때 (POST로 입력 되면)
    ##############################################################
    print("입력 방식", request.method)
    print("form submit", form.validate_on_submit())
    if request.method == 'POST' and form.validate_on_submit():
        sql = f"select * from user where username='{form.username.data}'"
        print(form.username)
        cur.execute(sql)
        user = cur.fetchone()
        print(user)
        if not user:
            sql = f"insert into user (username, password, email) values ('{form.username.data}','{generate_password_hash(form.password1.data)}','{form.email.data}');"
            cur.execute(sql)
            conn.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    print("submit 다음")
    ##############################################################
    return render_template("register.html", form=form)



@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    print("form 확인", form)
    print(form.username.data)
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        sql = f"select * from user where username='{form.username.data}'"
        cur.execute(sql)
        user = cur.fetchone() # fetchall()[0]을 사용하게 되면 인덱싱 에러로 인해 요구하는 에러 문구가 나타나지 않는다.
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user['password'], form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('login.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = {'user_id': session.get('user_id'), 'username': session['username']}
        print(g.user)

@bp.route('/logout/')
def logout() :
    session.clear()
    return redirect(url_for("main.index"))