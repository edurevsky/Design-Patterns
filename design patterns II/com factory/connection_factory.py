import MySQLdb

def get_connection(): # Design pattern factory
    connection = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="",
            db="alura"
    )
    return connection