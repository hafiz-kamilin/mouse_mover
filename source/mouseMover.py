#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Mohd Hafizuddin Bin Kamilin"

# load gui module
from PyQt5 import QtCore, QtGui, QtWidgets
# emulate a mouse for this program to control
from pynput.mouse import Controller
# randomizing the movement value
from random import randint
# sleep wait
from time import sleep
# to create a non-blocking gui
import threading
# load system specific function
import sys

# match up the icon on windows
import ctypes
myappid = u"mycompany.myproduct.subproduct.version"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


# GUI class
class Ui_MainWindow(QtWidgets.QMainWindow):

    # for opening the github link
    def link(self, linkStr):

        QtGui.QDesktopServices.openUrl(QtCore.QUrl(linkStr))

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(339, 171)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/mouse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(10, 10, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 321, 121))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 301, 43))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_timeSetExplanation_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_timeSetExplanation_2.setMinimumSize(QtCore.QSize(0, 13))
        self.label_timeSetExplanation_2.setSizeIncrement(QtCore.QSize(0, 13))
        self.label_timeSetExplanation_2.setObjectName("label_timeSetExplanation_2")
        self.verticalLayout_2.addWidget(self.label_timeSetExplanation_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBox_triggerInterval_1 = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox_triggerInterval_1.setMinimumSize(QtCore.QSize(44, 20))
        self.spinBox_triggerInterval_1.setMaximumSize(QtCore.QSize(44, 20))
        self.spinBox_triggerInterval_1.setProperty("value", 1)
        self.spinBox_triggerInterval_1.setMinimum(1)
        self.spinBox_triggerInterval_1.setObjectName("spinBox_triggerInterval_1")
        self.horizontalLayout_2.addWidget(self.spinBox_triggerInterval_1)
        self.label_triggerInterval_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_triggerInterval_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_triggerInterval_2.setObjectName("label_triggerInterval_2")
        self.horizontalLayout_2.addWidget(self.label_triggerInterval_2)
        self.spinBox_triggerInterval_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox_triggerInterval_2.setMinimumSize(QtCore.QSize(44, 20))
        self.spinBox_triggerInterval_2.setMaximumSize(QtCore.QSize(44, 20))
        self.spinBox_triggerInterval_2.setProperty("value", 3)
        self.spinBox_triggerInterval_2.setObjectName("spinBox_triggerInterval_2")
        self.horizontalLayout_2.addWidget(self.spinBox_triggerInterval_2)
        self.label_triggerInterval_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_triggerInterval_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_triggerInterval_3.setObjectName("label_triggerInterval_3")
        self.horizontalLayout_2.addWidget(self.label_triggerInterval_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pushButton_start = QtWidgets.QPushButton(self.tab)
        self.pushButton_start.setGeometry(QtCore.QRect(90, 70, 75, 23))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(self.tab)
        self.pushButton_stop.setGeometry(QtCore.QRect(170, 70, 75, 23))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 231, 21))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_source = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_source.setFont(font)
        self.label_source.setWordWrap(True)
        self.label_source.setObjectName("label_source")
        self.horizontalLayout.addWidget(self.label_source)
        self.label_urlDownload = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_urlDownload.setFont(font)
        self.label_urlDownload.setTextFormat(QtCore.Qt.AutoText)
        self.label_urlDownload.setOpenExternalLinks(True)
        self.label_urlDownload.setObjectName("label_urlDownload")
        self.horizontalLayout.addWidget(self.label_urlDownload)
        self.label_softwareExplanation = QtWidgets.QLabel(self.tab_2)
        self.label_softwareExplanation.setGeometry(QtCore.QRect(10, 10, 291, 51))
        self.label_softwareExplanation.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_softwareExplanation.setWordWrap(True)
        self.label_softwareExplanation.setObjectName("label_softwareExplanation")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # show the mouse mover is active or not
        self.stateIsActive = False
        # initialize the mouse object
        self.mouse = Controller()

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mouse Mover v0.0.1"))
        self.label_title.setText(_translate("MainWindow", "M²: Mouse Mover"))
        self.label_timeSetExplanation_2.setText(_translate("MainWindow", "Set the time trigger for the mouse to move/scroll between"))
        self.label_triggerInterval_2.setText(_translate("MainWindow", " to "))
        self.label_triggerInterval_3.setText(_translate("MainWindow", "minutes"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Configuration"))
        self.label_source.setText(_translate("MainWindow", "Source:"))
        self.label_urlDownload.setText('<a href="https://github.com/hafiz-kamilin/mouse_mover">https://github.com/hafiz-kamilin/mouse_mover/</a>')
        self.label_softwareExplanation.setText(_translate("MainWindow", "This software keeps your online status on Team, Skype, Discord, and any other applications that monitor the mouse movement."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "About"))

        # disable the stop button
        self.pushButton_stop.setEnabled(False)

        # define the threading for the mouseMover
        self.threadingMouseMover = threading.Thread(target=self.mouseMover)
        self.threadingMouseMover.daemon = True
        self.firstStart = True

        # when "start" button is pressed
        self.pushButton_start.clicked.connect(self.threadingManager)
        # when "stop" button is pressed
        self.pushButton_stop.clicked.connect(self.stopTheMover)

    # manage the threading
    def threadingManager(self):

        # disable the "start" button, enable the "stop" button
        self.pushButton_start.setEnabled(False)
        self.pushButton_stop.setEnabled(True)

        # if this is the first time the threading are activated
        if (self.firstStart is True):

            # start the process normally
            self.threadingMouseMover.start()
            self.firstStart = False

        else:

            # delete the threading declaration because we cannot restart the same thread
            del self.threadingMouseMover
            # re-declare the threading again
            self.threadingMouseMover = threading.Thread(target=self.mouseMover)
            self.threadingMouseMover.daemon = True
            # start normally
            self.threadingMouseMover.start()

    # function to move/scroll the mouse randomly
    def mouseMover(self):

        print("Waiting to move/scroll the mouse")
        # randomize the interval time
        sleepTimer = randint(self.spinBox_triggerInterval_1.value() * 60, self.spinBox_triggerInterval_2.value() * 60)
        print("Waiting time: " + str(sleepTimer) + "s")
        sleepTimer /= 0.1
        counterDuration = 0
        counterSleep = 0
        # change the state to active
        self.stateIsActive = True

        while self.stateIsActive is True:

            if (sleepTimer == counterSleep):

                # flip the coin; head (0) = scroll; tail (1) = move
                flipCoin = randint(0, 1)

                if (flipCoin == 0):

                    # scroll the mouse
                    self.mouse.scroll = (0, randint(1, 1000))
                    print("Mouse scrolled")
                
                else:

                    # move the mouse
                    self.mouse.position = (randint(200, 600), randint(2, 600))
                    print("Mouse moved")

                sleepTimer = randint(self.spinBox_triggerInterval_1.value() * 60, self.spinBox_triggerInterval_2.value() * 60)
                print("Waiting time: " + str(sleepTimer) + "s")
                counterSleep = 0
            
            else:

                counterSleep += 1
                counterDuration += 1

            sleep(0.1)

    # change stateIsActive to False if True and reset the button
    def stopTheMover(self):

        if (self.stateIsActive is True):

            self.stateIsActive = False
            print("Cancelled")

        # enable the "start" button, disable the "stop" button
        self.pushButton_start.setEnabled(True)
        self.pushButton_stop.setEnabled(False)

# initiator
if __name__ == "__main__":

    # initialize the GUI
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # show the GUI
    MainWindow.show()
    # exit the GUI (program)
    sys.exit(app.exec_())