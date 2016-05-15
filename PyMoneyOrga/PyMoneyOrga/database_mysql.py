import mysql.connector
from mysql.connector import Error

class Database(object):
    """description of class"""
    def connect():
        """ Connect to MySQL database """
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='python_mysql',
                                           user='root',
                                           password='secret')
            if conn.is_connected():
                print('Connected to MySQL database')
 
        except Error as e:
            print(e)
 
        finally:
            conn.close()

