# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\res\window_about.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import bdl


class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(379, 253)
        aboutDialog.setMinimumSize(QtCore.QSize(379, 253))
        aboutDialog.setMaximumSize(QtCore.QSize(379, 253))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ui/BDL_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutDialog.setWindowIcon(icon)
        aboutDialog.setStyleSheet("QDialog {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(50, 50, 50, 255), stop:1 rgba(85, 0, 0, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(32, 32, 32, 255), stop:1 rgba(64, 0, 0, 255));\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(aboutDialog)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, -1)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.bdlLabel = QtWidgets.QLabel(aboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bdlLabel.sizePolicy().hasHeightForWidth())
        self.bdlLabel.setSizePolicy(sizePolicy)
        self.bdlLabel.setMaximumSize(QtCore.QSize(96, 96))
        self.bdlLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bdlLabel.setAutoFillBackground(False)
        self.bdlLabel.setText("")
        self.bdlLabel.setTextFormat(QtCore.Qt.PlainText)
        self.bdlLabel.setPixmap(QtGui.QPixmap(":/ui/BDL_icon.ico"))
        self.bdlLabel.setScaledContents(True)
        self.bdlLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.bdlLabel.setWordWrap(True)
        self.bdlLabel.setObjectName("bdlLabel")
        self.gridLayout.addWidget(self.bdlLabel, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(aboutDialog)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 2)
        self.okButton = QtWidgets.QDialogButtonBox(aboutDialog)
        self.okButton.setOrientation(QtCore.Qt.Horizontal)
        self.okButton.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.okButton.setCenterButtons(True)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 6, 0, 1, 2)
        self.label = QtWidgets.QLabel(aboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(aboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("QLabel {\n"
"color: white;\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(2, 10, -1, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.versionLabel = QtWidgets.QLabel(aboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionLabel.sizePolicy().hasHeightForWidth())
        self.versionLabel.setSizePolicy(sizePolicy)
        self.versionLabel.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.versionLabel.setFont(font)
        self.versionLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.versionLabel.setStyleSheet("QLabel {\n"
"color: white;\n"
"}")
        self.versionLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.versionLabel.setWordWrap(False)
        self.versionLabel.setIndent(0)
        self.versionLabel.setOpenExternalLinks(True)
        self.versionLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.versionLabel.setObjectName("versionLabel")
        self.verticalLayout.addWidget(self.versionLabel)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.retranslateUi(aboutDialog)
        self.okButton.accepted.connect(aboutDialog.accept)
        self.okButton.rejected.connect(aboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About bdl"))
        self.label.setText(_translate("aboutDialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Special thanks to BioHazard for the original ZDoom Launcher (ZDL), QBasicer (qZDL), Lcferrum (ZDL revival), bloodbat (ZDoom Executer), Tony Phelps (ZDoom Runner), Hypnotoad90 (Rocket Launcher 2.0), hobomaster22 (Doom Launcher), and you! c:</span></p></body></html>"))
        self.label_4.setText(_translate("aboutDialog", "<html><head/><body><p style=\"line-height:0.25\">github: <a href=\"https://www.github.com/thisismy-github/bdl\"><span style=\" text-decoration: underline; color:#00aaff;\">https://www.github.com/thisismy-github/bdl</span></a></p><p>Any feedback? <a href=\"https://www.doomworld.com/messenger/compose/?to=28294\"><span style=\" text-decoration: underline; color:#00aaff;\">PM me on Doomworld</span></a></p></body></html>"))
        self.versionLabel.setText(_translate("aboutDialog", "<html><head/><body><p style=\"line-height:0.65\">bdl "+bdl.bdl.bdlVersionStr+"</p><p style=\"line-height:0.22\"><span style=\" font-size:10.5pt;\">copyright (c) 2020 me__</span></p><p><a href=\"https://www.thisismywebsite.net/\"><span style=\" font-size:10.5pt; text-decoration: underline; color:#00aaff;\">https://www.thisismywebsite.net/</span></a></p></body></html>"))
import res_rc
