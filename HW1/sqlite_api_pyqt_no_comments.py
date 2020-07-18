from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def main():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("db-api.db")
    db.open()
    query = QSqlQuery()
    query.exec_("DROP TABLE IF EXISTS test")
    query.exec_("CREATE TABLE test (id INTEGER PRIMARY KEY, string TEXT, number INTEGER)")
    query.exec_("INSERT INTO test (string, number) VALUES ('one', 1)")
    query.exec_("INSERT INTO test (string, number) VALUES ('two', 3)")
    query.exec_("INSERT INTO test (string, number) VALUES ('three', 3)")
    query.exec_("SELECT * FROM test")
    print(query)    # imprime <PyQt5.QtSql.QSqlQuery object at 0x00000242894C5828>
    while query.next():
        print((query.value(0), query.value(1), query.value(3)))
    db.close()


if __name__ == '__main__': main()
