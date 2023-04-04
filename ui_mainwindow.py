# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 291)
        MainWindow.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 9)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.summframe = QtWidgets.QFrame(parent=self.centralwidget)
        self.summframe.setMinimumSize(QtCore.QSize(0, 50))
        self.summframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.summframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.summframe.setObjectName("summframe")
        self.verticalLayout.addWidget(self.summframe)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setEnabled(False)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/exit.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionQuit.setIcon(icon)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_Qt = QtGui.QAction(parent=MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionTool_bar = QtGui.QAction(parent=MainWindow)
        self.actionTool_bar.setObjectName("actionTool_bar")
        self.actionStatus_bar = QtGui.QAction(parent=MainWindow)
        self.actionStatus_bar.setObjectName("actionStatus_bar")
        self.actionAddWorkout = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/add.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAddWorkout.setIcon(icon1)
        self.actionAddWorkout.setObjectName("actionAddWorkout")
        self.actionDeleteWorkout = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/delete.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionDeleteWorkout.setIcon(icon2)
        self.actionDeleteWorkout.setObjectName("actionDeleteWorkout")
        self.actionSubmit = QtGui.QAction(parent=MainWindow)
        self.actionSubmit.setObjectName("actionSubmit")
        self.actionRevert = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/revert.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRevert.setIcon(icon3)
        self.actionRevert.setObjectName("actionRevert")
        self.actionWorkoutType = QtGui.QAction(parent=MainWindow)
        self.actionWorkoutType.setObjectName("actionWorkoutType")
        self.actionSettings = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSettings.setIcon(icon4)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionTool_bar)
        self.menuView.addAction(self.actionStatus_bar)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuEdit.addAction(self.actionAddWorkout)
        self.menuEdit.addAction(self.actionDeleteWorkout)
        self.menuEdit.addAction(self.actionSubmit)
        self.menuEdit.addAction(self.actionRevert)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionWorkoutType)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt"))
        self.actionTool_bar.setText(_translate("MainWindow", "Tool bar"))
        self.actionStatus_bar.setText(_translate("MainWindow", "Status bar"))
        self.actionAddWorkout.setText(_translate("MainWindow", "Add workout"))
        self.actionDeleteWorkout.setText(_translate("MainWindow", "Delete workout"))
        self.actionSubmit.setText(_translate("MainWindow", "Submit"))
        self.actionRevert.setText(_translate("MainWindow", "Revert"))
        self.actionWorkoutType.setText(_translate("MainWindow", "Workout type"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
