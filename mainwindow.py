from PyQt6.QtCore import Qt, QSettings
# from PyQt6.QtGui import
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QToolBar, QLabel
from PyQt6.QtSql import QSqlRelationalDelegate

import ui_mainwindow

from database import Database
from tabedit import TabEdit

db_filename = "./workouts.sl3"


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.ui = ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        mainToolBar = QToolBar("MainToolBar")
        mainToolBar.setObjectName('MainToolBar')
        mainToolBar.addAction(self.ui.actionAddWorkout)
        mainToolBar.addAction(self.ui.actionDeleteWorkout)
        mainToolBar.addAction(self.ui.actionSubmit)
        mainToolBar.addAction(self.ui.actionRevert)
        self.addToolBar(mainToolBar)

        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionAddWorkout.triggered.connect(self.addWorkout)
        self.ui.actionDeleteWorkout.triggered.connect(self.deleteWorkout)
        self.ui.actionSubmit.triggered.connect(self.submit)
        self.ui.actionRevert.triggered.connect(self.revert)
        self.ui.actionWorkoutType.triggered.connect(self.workoutType)

        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionAbout_Qt.triggered.connect(self.aboutQt)

        self.copyright = '<p><span style="font-size:10pt; color:#000055;">Copyright &copy; 2023 big-pond (George)</span></p>'
        self.ui.statusbar.addWidget(QLabel(self.copyright))
        self.db = Database()
        if self.db.connectToDatabase(db_filename):
            self.setCurretFile(db_filename)

            self.model = self.db.initWorkoutModel()
            self.model.dataChanged.connect(self.updateActions)
            self.ui.tableView.setModel(self.model)
            self.ui.tableView.setItemDelegate(QSqlRelationalDelegate(self.ui.tableView))
            self.ui.tableView.horizontalHeader().stretchLastSection()
            while self.model.canFetchMore():
                self.model.fetchMore()
            self.ui.tableView.setCurrentIndex(self.model.index(self.model.rowCount()-1, 1))
            self.updateActions()
        self.readSettings()

    def closeEvent(self, event):
        self.writeSettings()
        QMainWindow.closeEvent(self, event)

    def readSettings(self):
        settings = QSettings('workouts.ini', QSettings.Format.IniFormat)
        settings.beginGroup('MainWindow')
        self.restoreGeometry(settings.value('geometry', self.saveGeometry()))
        self.restoreState(settings.value('windowState', self.saveState()))
        settings.endGroup()

    def writeSettings(self):
        settings = QSettings('workouts.ini', QSettings.Format.IniFormat)
        settings.beginGroup('MainWindow')
        settings.setValue('geometry', self.saveGeometry())
        settings.setValue('windowState', self.saveState())
        settings.endGroup()

    def addWorkout(self):
        row = self.model.rowCount()
        success = self.model.insertRow(row)
        self.ui.tableView.setCurrentIndex(self.model.index(row, 1))
        self.updateActions()
        return success

    def deleteWorkout(self):
        result = False
        index = self.ui.tableView.currentIndex()
        if index.isValid():
            result = self.model.removeRow(index.row())
            self.updateActions()
        return result

    def submit(self):
        self.model.submitAll()
        while self.model.canFetchMore():
            self.model.fetchMore()
        self.ui.tableView.setCurrentIndex(self.model.index(self.model.rowCount()-1, 1))
        self.updateActions()

    def revert(self):
        self.model.revertAll()

    def workoutType(self):
        dlg = TabEdit()
        dlg.setWindowTitle(self.tr('Workout types'))
        model = self.db.initTypeModel()
        dlg.setModel(model)
        dlg.exec()

    def about(self):
        QMessageBox.about(self, self.tr('About'),
                          '''<h2 align="center"><font color="#008000">workouts 1.0</font></h2>
<p align="center"><font color="#000080" face="Times New Roman" size="4">
<b>My rare workouts</b></font></p><p>{0}</p>
        '''.format(self.copyright))

    def aboutQt(self):
        QMessageBox.aboutQt(self)

    def setCurretFile(self, file_name):
        # db_filename = file_name
        self.setWindowTitle(db_filename)

    def updateActions(self):
        dirty = self.model.isDirty()
        self.ui.actionSubmit.setEnabled(dirty)
        self.ui.actionRevert.setEnabled(dirty)

