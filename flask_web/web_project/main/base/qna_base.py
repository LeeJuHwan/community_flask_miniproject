from flask import Blueprint, render_template
from ..db import conn, cur

bp = Blueprint('qna', __name__, url_prefix='/qna')

@bp.route('/')
def qna() :
	# print("에러 확인")
	# sql = 'SELECT * FROM board;'
	# cur.execute(sql)
	# board_list = cur.fetchall()
	# print(board_list)
	return render_template('QNA.html')



@bp.route('/faq')
def faq() :
	# print("에러 확인")
	# sql = 'SELECT * FROM board;'
	# cur.execute(sql)
	# board_list = cur.fetchall()
	# print(board_list)
	return render_template('FAQ.html')

