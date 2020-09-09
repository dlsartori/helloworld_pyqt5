from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5 import uic
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = uic.loadUi("dialog_form.ui")

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("GanadoSQLite.db")
    db.open()
    query = QSqlQuery()
    query.exec_("SELECT * FROM Animales")
    model = QSqlTableModel()
    model.setTable("Animales")
    model.setQuery(query)
    window.tableView1.setModel(model)

    window.show()
    sys.exit(app.exec_())

