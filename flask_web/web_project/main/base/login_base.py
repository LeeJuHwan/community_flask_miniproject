from flask import Blueprint, url_for, render_template, flash, request, session, g, redirect
from ..form import UserCreateForm
from ..db import conn, cur
from werkzeug.security import generate_password_hash, check_password_hash

# 블루프린트 생성
bp = Blueprint('user', __name__, url_prefix='/user')

# 회원가입 
@bp.route('/login/', methods=('GET', 'POST'))
def log():
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
    return render_template("login.html", form=form)