from pymysql import cursors, connect

conn = connect(host = "localhost", user="root", passwd="qhdkscjfwj0!", db ="project", charset = "utf8", cursorclass=cursors.DictCursor)
cur = conn.cursor()
