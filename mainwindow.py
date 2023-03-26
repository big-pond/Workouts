from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QMainWindow, QMessageBox

import ui_mainwindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.ui = ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionQuit.triggered.connect(self.close)

        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionAbout_Qt.triggered.connect(self.aboutQt)

        self.copyright = '<p><span style="font-size:10pt; color:#000055;">Copyright &copy; 2023 big-pond (George)</span></p>'

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