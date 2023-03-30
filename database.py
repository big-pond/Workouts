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
            print("Не удалось восстановить базу данных")
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
