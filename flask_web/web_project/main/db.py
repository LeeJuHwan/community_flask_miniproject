from pymysql import cursors, connect

conn = connect(host = "localhost", user="root", passwd="pass123#", db ="pybo", charset = "utf8", cursorclass=cursors.DictCursor)
cur = conn.cursor()
