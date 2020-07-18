from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def main():
    # Crear la conexión como un objeto que apunta al archivo "db-api.db"
    # Si no existe db-api.db, lo crea
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("db-api.db")
    db.open()

    # Crear el objeto "query" (QSqlQuery), similar al cursor de la API SQLite de Python
    query = QSqlQuery()

    # Ejecutar sentencias SQL mediante el método exec_() del objeto QSqlQuery
    # En este caso son sentencias de escritura (CREATE, INSERT)
    #   Borrar la tabla "test", si es que existe
    query.exec_("DROP TABLE IF EXISTS test")
    #   Crear la tabla "test"
    query.exec_("CREATE TABLE test (id INTEGER PRIMARY KEY, string TEXT, number INTEGER)")
    #   Insertar un registro
    #   Solo se pasan los valores de los campos "string" y "number"
    #   El campo "id" es primary key, se autoincrementa
    query.exec_("INSERT INTO test (string, number) VALUES ('one', 1)")
    #   Insertar otro registro
    query.exec_("INSERT INTO test (string, number) VALUES ('two', 3)")
    #   Insertar otro registro más
    query.exec_("INSERT INTO test (string, number) VALUES ('three', 3)")

    # Acá no hace falta confirmar los cambios de las sentencias de escritura
    # Se escriben automáticamente en el archivo "db-api.db"

    # Ejecutar sentencia SQL mediante el método exec_() del objeto QSqlQuery
    # En este caso es una sentencias de lectura (SELECT)
    query.exec_("SELECT * FROM test")

    # Los 6 pasos anteriores se pueden hacer también mediante el método exec() del objeto "db" (QSqlDatabase)
    # db.exec("DROP TABLE IF EXISTS test")
    # db.exec("CREATE TABLE test (id INTEGER PRIMARY KEY, string TEXT, number INTEGER)")
    # db.exec("INSERT INTO test (string, number) VALUES ('one', 1)")
    # db.exec("INSERT INTO test (string, number) VALUES ('two', 3)")
    # db.exec("INSERT INTO test (string, number) VALUES ('three', 3)")
    # query = db.exec("SELECT * FROM test")

    print(query)    # imprime <PyQt5.QtSql.QSqlQuery object at 0x00000242894C5828>

    # El objeto QSqlQuery es iterable, se lo recorre mediante un loop
    while query.next():
        print((query.value(0), query.value(1), query.value(3)))
    # imprime:
    #   (1, 'one', None)
    #   (2, 'two', None)
    #   (3, 'three', None)

    # Cerrar la conexión (destruir el objeto "db")
    db.close()

if __name__ == '__main__': main()
