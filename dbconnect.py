import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "automataanywhere",
                           passwd = "niermankind6o",
                           db = "automataanhywhere$pythonprogramming"
                           )
    c = conn.cursor()

    return c, conn