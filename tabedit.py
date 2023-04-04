from PyQt6.QtWidgets import QDialog

import ui_tabedit


class TabEdit(QDialog):

    def __init__(self, parent=None):
        super(QDialog, self).__init__()
        self.ui = ui_tabedit.Ui_TabEdit()
        self.ui.setupUi(self)
        self.ui.tbAdd.clicked.connect(self.addRecord)
        self.ui.tbDel.clicked.connect(self.deleteRecord)
        self.ui.tbSubmit.clicked.connect(self.submit)
        self.ui.tbRevert.clicked.connect(self.revert)


    def setModel(self, model):
        self.ui.tableView.setModel(model)

    def isBookModelChanged(self):
        return self.ui.tableView.model.isDirty()

    def addRecord(self):
        success = self.ui.tableView.model.insertRow(self.ui.tableView.model.rowCount())
        return success

    def deleteRecord(self):
        index = self.ui.tableView.currentIndex()
        if index.isValid():
            result = self.ui.tableView.model.removeRow(index.row())
        return result

    def submit(self):
        self.ui.tableView.model.submitAll()

    def revert(self):
        self.ui.tableView.model.revertAll()
