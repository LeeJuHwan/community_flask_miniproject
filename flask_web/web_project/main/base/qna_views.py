from flask import Blueprint, render_template
from ..db import conn, cur

bp = Blueprint('qna', __name__, url_prefix='/qna')

@bp.route('/')
def qna_1() :
	sql = 'SELECT * FROM faq;'
	cur.execute(sql)
	qna_list = cur.fetchall()


	return render_template('qnapage.html',qna_list=qna_list)

