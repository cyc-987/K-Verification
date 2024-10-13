# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_imput_area = QtWidgets.QFrame(self.centralwidget)
        self.frame_imput_area.setGeometry(QtCore.QRect(-1, -1, 801, 351))
        self.frame_imput_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_imput_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_imput_area.setObjectName("frame_imput_area")
        self.layoutWidget = QtWidgets.QWidget(self.frame_imput_area)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 120, 721, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.password1 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password1.sizePolicy().hasHeightForWidth())
        self.password1.setSizePolicy(sizePolicy)
        self.password1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password1.setObjectName("password1")
        self.horizontalLayout_2.addWidget(self.password1)
        self.password2 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password2.sizePolicy().hasHeightForWidth())
        self.password2.setSizePolicy(sizePolicy)
        self.password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password2.setObjectName("password2")
        self.horizontalLayout_2.addWidget(self.password2)
        self.password3 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password3.sizePolicy().hasHeightForWidth())
        self.password3.setSizePolicy(sizePolicy)
        self.password3.setText("")
        self.password3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password3.setObjectName("password3")
        self.horizontalLayout_2.addWidget(self.password3)
        self.password4 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password4.sizePolicy().hasHeightForWidth())
        self.password4.setSizePolicy(sizePolicy)
        self.password4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password4.setObjectName("password4")
        self.horizontalLayout_2.addWidget(self.password4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(150, 0, 150, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clearButton = QtWidgets.QPushButton(self.layoutWidget)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.enterButton = QtWidgets.QPushButton(self.layoutWidget)
        self.enterButton.setObjectName("enterButton")
        self.horizontalLayout.addWidget(self.enterButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.frame_information_area = QtWidgets.QFrame(self.centralwidget)
        self.frame_information_area.setGeometry(QtCore.QRect(-1, 349, 401, 211))
        self.frame_information_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_information_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_information_area.setObjectName("frame_information_area")
        self.frame_settings_area = QtWidgets.QFrame(self.centralwidget)
        self.frame_settings_area.setGeometry(QtCore.QRect(399, 349, 401, 211))
        self.frame_settings_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_settings_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_settings_area.setObjectName("frame_settings_area")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_settings_area)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 361, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_select_port = QtWidgets.QLabel(self.layoutWidget1)
        self.label_select_port.setAlignment(QtCore.Qt.AlignCenter)
        self.label_select_port.setObjectName("label_select_port")
        self.horizontalLayout_3.addWidget(self.label_select_port)
        self.comboBox_port = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_port.setObjectName("comboBox_port")
        self.horizontalLayout_3.addWidget(self.comboBox_port)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_settings_area)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 40, 361, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_connect_status = QtWidgets.QLabel(self.layoutWidget2)
        self.label_connect_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_connect_status.setObjectName("label_connect_status")
        self.horizontalLayout_4.addWidget(self.label_connect_status)
        self.refreshButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_4.addWidget(self.refreshButton)
        self.connectButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_4.addWidget(self.connectButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionGithub_Repo = QtWidgets.QAction(MainWindow)
        self.actionGithub_Repo.setObjectName("actionGithub_Repo")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.menuOptions.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionGithub_Repo)
        self.menuAbout.addAction(self.actionVersion)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close) # type: ignore
        self.clearButton.clicked.connect(self.password1.clear) # type: ignore
        self.enterButton.clicked.connect(MainWindow.printContent) # type: ignore
        self.actionVersion.triggered.connect(MainWindow.showAbout) # type: ignore
        self.clearButton.clicked.connect(self.password2.clear) # type: ignore
        self.clearButton.clicked.connect(self.password3.clear) # type: ignore
        self.clearButton.clicked.connect(self.password4.clear) # type: ignore
        self.refreshButton.clicked.connect(MainWindow.getAvailablePorts) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "K Verification-Insider Preview-Ver 0.0.1"))
        self.password1.setPlaceholderText(_translate("MainWindow", "part1"))
        self.password2.setPlaceholderText(_translate("MainWindow", "part2"))
        self.password3.setPlaceholderText(_translate("MainWindow", "part3"))
        self.password4.setPlaceholderText(_translate("MainWindow", "part4"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.enterButton.setText(_translate("MainWindow", "Confirm"))
        self.label_select_port.setText(_translate("MainWindow", "Select Port"))
        self.label_connect_status.setText(_translate("MainWindow", "No connection"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionGithub_Repo.setText(_translate("MainWindow", "Github Repo"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
