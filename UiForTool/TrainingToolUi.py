# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrainingToolUi.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1132, 825)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 1111, 781))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.StartTraining = QPushButton(self.gridLayoutWidget)
        self.StartTraining.setObjectName(u"StartTraining")

        self.gridLayout.addWidget(self.StartTraining, 2, 0, 1, 1)

        self.NewImageSetter = QPushButton(self.gridLayoutWidget)
        self.NewImageSetter.setObjectName(u"NewImageSetter")

        self.gridLayout.addWidget(self.NewImageSetter, 1, 0, 1, 1)

        self.imageShower = QLabel(self.gridLayoutWidget)
        self.imageShower.setObjectName(u"imageShower")
        self.imageShower.setLayoutDirection(Qt.LeftToRight)
        self.imageShower.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.imageShower, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1132, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.StartTraining.setText(QCoreApplication.translate("MainWindow", u"\n"
"Train\n"
"", None))
        self.NewImageSetter.setText(QCoreApplication.translate("MainWindow", u"\n"
"Set new image\n"
"", None))
        self.imageShower.setText(QCoreApplication.translate("MainWindow", u"Here you will se your image", None))
    # retranslateUi

