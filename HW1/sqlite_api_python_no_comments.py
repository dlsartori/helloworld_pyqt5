import sqlite3


def main():
    db = sqlite3.connect('db-api.db')
    cur = db.cursor()
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, string TEXT, number INTEGER)")
    cur.execute("INSERT INTO test (string, number) VALUES ('one', 1)")
    cur.execute("INSERT INTO test (string, number) VALUES ('two', 2)")
    cur.execute("INSERT INTO test (string, number) VALUES ('three', 3)")
    db.commit()
    cur.execute("SELECT * FROM test")
    print(cur)
    result1row = cur.fetchone();
    print(result1row)
    resultAllRows = cur.fetchall();
    print(resultAllRows)
    db.close()


if __name__ == '__main__': main()
