from pymysql import cursors, connect

conn = connect(host = "localhost", user="root", passwd="1111", db ="project", charset = "utf8", cursorclass=cursors.DictCursor)
cur = conn.cursor()
