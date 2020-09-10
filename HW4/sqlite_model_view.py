from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlRelationalTableModel, QSqlRelation
from PyQt5 import uic
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('windows')
    window = uic.loadUi("dialog_form.ui")

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("geo.db")
    db.open()
    # model = QSqlRelationalTableModel()
    # model.setTable("Departamentos")
    # model.setRelation(1, QSqlRelation("Provincias", "ID_Provincia", "[Nombre Provincia]"))
    # model.select()
    model = QSqlTableModel()
    # query = QSqlQuery()
    # query.exec_("SELECT * FROM Departamentos")
    # model.setQuery(query)
    model.setTable("Departamentos")
    model.select()
    window.tableView1.setModel(model)

    window.show()
    sys.exit(app.exec_())
