from PyQt6.QtCore import Qt, QObject, QFileInfo
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelationalTableModel, QSqlRelation


class Database(QObject):
    def __init__(self, parent=None):
        super(QObject, self).__init__()
        self.db = QSqlDatabase.addDatabase("QSQLITE", "MAIN")

    def connectToDatabase(self, file_name):
        result = False
        if not QFileInfo.exists(file_name):
            result = self.restoreDatabase(file_name)
        else:
            result = self.openDatabase(file_name)
        return result

    def restoreDatabase(self, file_name):
        result = True
        if self.openDatabase(file_name):
            self.createTables()
        else:
            print("The database could not be restored.")
            result = False
        return result

    def openDatabase(self, file_name):
        # self.db.setHostName(DATABASE_HOSTNAME)
        self.db.setDatabaseName(file_name)
        result = self.db.open()
        return result

    def closeDatabase(self):
        self.db.close()

    def createTables(self):
        with open('./resources/createdb.sql', 'rt') as file:
            qwery_list = file.readlines()

        query = QSqlQuery(self.db)
        for s in qwery_list:
            s = s.strip()
            if len(s) > 0:
                query.exec(s)

    def getDb(self):
        return self.db

    def initWorkoutModel(self):
        model = QSqlRelationalTableModel(db=self.db)
        model.setTable("workout")

        model.setJoinMode(QSqlRelationalTableModel.JoinMode.LeftJoin)
        model.setEditStrategy(QSqlRelationalTableModel.EditStrategy.OnManualSubmit)

        model.setRelation(1, QSqlRelation("typew", "id", "name"))
        model.relationModel(1).sort(1, Qt.SortOrder.AscendingOrder)

        model.setHeaderData(0, Qt.Orientation.Horizontal, "id")
        model.setHeaderData(1, Qt.Orientation.Horizontal, self.tr("Type"))
        model.setHeaderData(2, Qt.Orientation.Horizontal, self.tr("Date"))
        model.setHeaderData(3, Qt.Orientation.Horizontal, self.tr("Distance"))
        model.setHeaderData(4, Qt.Orientation.Horizontal, self.tr("Note"))

        model.select()
        return model

