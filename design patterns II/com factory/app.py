# Exemplo
import MySQLdb
from connection_factory import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute("SELECT * from cursos")

for linha in cursor:
    print(linha)

connection.close()