#Ejemplo de conexion SQLITE3 
from multiprocessing import current_process
import sqlite3

def main():
    
    #Nos conectamos a la bbdd
    conn = sqlite3.connect('database.db')
    #Creamos un cursor
    cursor = conn.cursor()
    #Leemos todos los datos de la bbdd
    rows = cursor.execute('SELECT * FROM users')
    
    #leemos los datos
    for row in rows:
        print(row)   
    #Cerramos el cursor
    cursor.close()
    
    cursor = conn.cursor()
    query = 'SELECT * FROM users WHERE id = 1'
    rows = cursor.execute(query)
    for row in rows:
        print(row)
    
    #Cerramos la conexion a la bbdd
    conn.close()
    




if __name__ == '__main__':
    main()