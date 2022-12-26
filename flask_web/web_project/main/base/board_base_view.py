from flask import Blueprint, render_template
from ..db import conn, cur

bp = Blueprint('board_base', __name__, url_prefix='/board_base')

@bp.route('/')
def board_1() :
	print("에러 확인")
	sql = 'SELECT * FROM board;'
	cur.execute(sql)
	board_list = cur.fetchall()
	print(board_list)

	return render_template('board.html',board_list=board_list)

