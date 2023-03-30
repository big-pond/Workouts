from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtSql import QSqlRelationalTableModel, QSqlRelation

import ui_mainwindow

from database import Database

db_filename = "./workouts.sl3"


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.ui = ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionQuit.triggered.connect(self.close)

        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionAbout_Qt.triggered.connect(self.aboutQt)

        self.copyright = '<p><span style="font-size:10pt; color:#000055;">Copyright &copy; 2023 big-pond (George)</span></p>'
        self.db = Database()
        if self.db.connectToDatabase(db_filename):
            self.setCurretFile(db_filename)

            self.model = QSqlRelationalTableModel(db=self.db.getDb())
            self.initWorkoutModel()
            self.ui.tableView.setModel(self.model)
            self.updateActions()

    def initWorkoutModel(self):
        self.model.setTable("workout")

        self.model.setJoinMode(QSqlRelationalTableModel.JoinMode.LeftJoin)
        self.model.setEditStrategy(QSqlRelationalTableModel.EditStrategy.OnManualSubmit)

        self.model.setRelation(1, QSqlRelation("typew", "id", "name"))
        self.model.relationModel(1).sort(1, Qt.SortOrder.AscendingOrder)

        self.model.setHeaderData(0, Qt.Orientation.Horizontal, "id")
        self.model.setHeaderData(1, Qt.Orientation.Horizontal, self.tr("Type"))
        self.model.setHeaderData(2, Qt.Orientation.Horizontal, self.tr("Distance"))
        self.model.setHeaderData(3, Qt.Orientation.Horizontal, self.tr("Note"))

        self.model.select()
        print(self.model.rowCount())

    def readSettings(self):
        settings = QSettings('workouts.ini', QSettings.Format.IniFormat)
        settings.beginGroup('MainWindow')
        is_geometry = settings.contains("geometry")
        if is_geometry:
            self.restoreGeometry(settings.value('geometry', ''))
        is_window_state = settings.contains("windowState")
        if is_window_state:
            self.restoreState(settings.value('windowState', ''))
        settings.endGroup()

    def writeSettings(self):
        settings = QSettings('workouts.ini', QSettings.Format.IniFormat)
        settings.beginGroup('MainWindow')
        settings.setValue('geometry', self.saveGeometry())
        settings.setValue('windowState', self.saveState())
        settings.endGroup()

    def about(self):
        QMessageBox.about(self, self.tr('About'),
                          '''<h2 align="center"><font color="#008000">workouts 1.0</font></h2>
<p align="center"><font color="#000080" face="Times New Roman" size="4">
<b>Gpx on map</b></font></p><p>{0}</p>
        '''.format(self.copyright))

    def aboutQt(self):
        QMessageBox.aboutQt(self)

    def setCurretFile(self, file_name):
        # db_filename = file_name
        self.setWindowTitle(db_filename)

    def updateActions(self):
        pass
