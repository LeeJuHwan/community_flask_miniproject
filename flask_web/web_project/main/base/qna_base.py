from flask import Blueprint, render_template
from ..db import conn, cur

bp = Blueprint('qna', __name__, url_prefix='/qna')

@bp.route('/')
def qna() :
	print("에러 확인")
	sql = 'SELECT id, title, content, date_format(create_date, "%Y-%m-%d") FROM qna order by id desc;'
	cur.execute(sql)
	board_list = cur.fetchall()
	print(board_list)
	return render_template('QNA.html',board_list=board_list)



@bp.route('/faq')
def faq() :
	print("에러 확인")
	sql = "select f.id, c.category, f.title, date_format(f.write_date, '%Y-%m-%d') as write_date from faq f join faq_category c on f.category_id = c.id order by f.id desc;"
	cur.execute(sql)
	faq_list = cur.fetchall()
	print(faq_list)
	return render_template('FAQ.html',faq_list=faq_list)

