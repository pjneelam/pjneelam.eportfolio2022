#https://www.youtube.com/watch?v=f9PR1qcwOyg
#create global convention 
import mysql.connector
__cnx=None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database='assignment2')
    return __cnx
    cnx.close()