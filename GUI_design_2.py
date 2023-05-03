# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gallery.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from screeninfo import get_monitors


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        for monitor in get_monitors():
            if(monitor.is_primary):
                width = monitor.width
                height = monitor.height
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(width, height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.previous_image_button = QtWidgets.QPushButton(self.centralwidget)
        self.previous_image_button.setGeometry(QtCore.QRect(90, int(height*0.8), 151, 51))
        self.previous_image_button.setObjectName("previous_image_button")
        self.next_image_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_image_button.setGeometry(QtCore.QRect(240, int(height*0.8), 151, 51))
        self.next_image_button.setObjectName("next_image_button")
        self.load_image_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_image_button.setGeometry(QtCore.QRect(170, int(height*0.8+51), 141, 41))
        self.load_image_button.setObjectName("load_image_button")
        self.display_image = QtWidgets.QLabel(self.centralwidget)
        self.display_image.setGeometry(QtCore.QRect(30, 40, int(width*0.8-51), int(height*0.8-51)))
        self.display_image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.display_image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.display_image.setLineWidth(20)
        self.display_image.setText("")
        self.display_image.setPixmap(QtGui.QPixmap("../imagis analysis/hw2_handout/cat.jpg"))
        self.display_image.setScaledContents(False)
        self.display_image.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.display_image.setWordWrap(False)
        self.display_image.setObjectName("display_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 26))
        self.menubar.setObjectName("menubar")
        self.menuside = QtWidgets.QMenu(self.menubar)
        self.menuside.setObjectName("menuside")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuside.addSeparator()
        self.menuside.addSeparator()
        self.menuside.addSeparator()
        self.menuside.addSeparator()
        self.menubar.addAction(self.menuside.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.previous_image_button.setText(_translate("MainWindow", "<"))
        self.next_image_button.setText(_translate("MainWindow", ">"))
        self.load_image_button.setText(_translate("MainWindow", "Load images"))
        self.menuside.setTitle(_translate("MainWindow", "side"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())