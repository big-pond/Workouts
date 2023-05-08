from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import QSettings

import ui_tabedit


class TabEdit(QDialog):

    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = ui_tabedit.Ui_TabEdit()
        self.ui.setupUi(self)
        self.ui.tbFirst.clicked.connect(self.first)
        self.ui.tbLast.clicked.connect(self.last)
        self.ui.tbAdd.clicked.connect(self.addRecord)
        self.ui.tbDel.clicked.connect(self.deleteRecord)
        self.ui.tbSubmit.clicked.connect(self.submit)
        self.ui.tbRevert.clicked.connect(self.revert)
        self.readSettings()

    def done(self, a0: int) -> None:
        self.writeSettings()
        QDialog.done(self, a0)

    def setModel(self, model):
        self.ui.tableView.setModel(model)

    def isBookModelChanged(self):
        return self.ui.tableView.model.isDirty()

    def first(self):
        self.ui.tableView.setCurrentIndex(self.ui.tableView.model.index(0, 2))

    def last(self):
        model = self.ui.tableView.model()
        row = model.rowCount()-1
        self.ui.tableView.setCurrentIndex(model.index(row, 1))

    def addRecord(self):
        model = self.ui.tableView.model()
        row = model.rowCount()
        model.insertRow(row)
        self.ui.tableView.setCurrentIndex(model.index(row, 1))

    def deleteRecord(self):
        index = self.ui.tableView.currentIndex()
        if index.isValid():
            self.ui.tableView.model().removeRow(index.row())
        else:
            QMessageBox.information(self, '', 'Record not delected.')

    def submit(self):
        self.ui.tableView.model().submitAll()

    def revert(self):
        self.ui.tableView.model().revertAll()

    def readSettings(self):
        settings = QSettings('workouts.ini', QSettings.Format.IniFormat)
        settings.beginGroup('TabEdit')
        self.restoreGeometry(settings.value('geometry', self.saveGeometry()))
        settings.endGroup()

    def writeSettings(self):
        settings = QSettings('workouts.ini', QSettings.Format.IniFormat)
        settings.beginGroup('TabEdit')
        settings.setValue('geometry', self.saveGeometry())
        settings.endGroup()
