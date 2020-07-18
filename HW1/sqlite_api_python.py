import sqlite3

def main():
    # Crear la conexión como un objeto que apunta al archivo "db-api.db"
    # Si no existe db-api.db, lo crea
    db = sqlite3.connect('db-api.db')
    
    # Crear el cursor
    cur = db.cursor()

    # Ejecutar sentencias SQL mediante el método execute() del cursor
    # En este caso son sentencias de escritura (CREATE, INSERT)
    #   Borrar la tabla "test", si es que existe
    cur.execute("DROP TABLE IF EXISTS test")
    #   Crear la tabla "test"
    cur.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, string TEXT, number INTEGER)")
    #   Insertar un registro
    #   Solo se pasan los valores de los campos "string" y "number"
    #   El campo "id" es primary key, se autoincrementa
    cur.execute("INSERT INTO test (string, number) VALUES ('one', 1)")
    #   Insertar otro registro
    cur.execute("INSERT INTO test (string, number) VALUES ('two', 2)")
    #   Insertar otro registro más
    cur.execute("INSERT INTO test (string, number) VALUES ('three', 3)")

    # Confirmar los cambios de las sentencias de escritura
    # Esto escribe en el archivo "db-api.db"
    db.commit()

    # Ejecutar sentencia SQL mediante el método execute() del cursor
    # En este caso es una sentencias de lectura (SELECT)
    cur.execute("SELECT * FROM test")
    print(cur)  # imprime <sqlite3.Cursor object at 0x0091B660>

    # El método fetchone() se mueve al próximo registro y devuelve una tupla con los valores
    result1row = cur.fetchone();
    print(result1row)   # imprime (1, 'one', 1)

    # El método fetchall() devuelve una lista de tuplas con los valores de los registros restantes
    resultAllRows = cur.fetchall();
    print(resultAllRows)    # imprime [(2, 'two', 2), (3, 'three', 3)]
    
    # Cerrar la conexión (destruir el objeto "db")
    db.close()

if __name__ == '__main__': main()
