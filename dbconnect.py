import MySQLdb
# hint how to create python anywhere connection code with mysql https://www.pythonanywhere.com/forums/topic/11305/
def connection():
    conn = MySQLdb.connect(host="automataanywhere.mysql.pythonanywhere-services.com",
                           user = "automataanywhere",
                           passwd = "niermankind6o",
                           db = "automataanywhere$pythonprogramming"
                           )
    c = conn.cursor()

    return c, conn