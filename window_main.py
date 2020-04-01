# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\res\window_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import window_about, run
import os, hashlib, configparser, webbrowser


class Ui_BDLMainWindow(object):
    def setupUi(self, BDLMainWindow):
        BDLMainWindow.setObjectName("BDLMainWindow")
        BDLMainWindow.resize(225, 247)
        BDLMainWindow.setAcceptDrops(True)
        BDLMainWindow.setWindowTitle("bdl")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ui/BDL_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BDLMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(BDLMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabWidget::pane { \n"
" position: absolute;\n"
" padding: 1px 1px 1px 1px;\n"
" margin: -8px -7px -8px -7px; }\n"
"\n"
"QTabBar::tab { padding: 2px 7px 0px 7px; }")
        self.tabWidget.setObjectName("tabWidget")
        self.tabMain = QtWidgets.QWidget()
        self.tabMain.setObjectName("tabMain")
        self.gridLayout = QtWidgets.QGridLayout(self.tabMain)
        self.gridLayout.setObjectName("gridLayout")
        self.tabMainGLayout = QtWidgets.QGridLayout()
        self.tabMainGLayout.setSpacing(0)
        self.tabMainGLayout.setObjectName("tabMainGLayout")
        self.bottomGLayout = QtWidgets.QVBoxLayout()
        self.bottomGLayout.setSpacing(1)
        self.bottomGLayout.setObjectName("bottomGLayout")
        self.splitter = QtWidgets.QSplitter(self.tabMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.leftVLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.leftVLayout.setContentsMargins(0, 0, 0, 0)
        self.leftVLayout.setSpacing(0)
        self.leftVLayout.setObjectName("leftVLayout")
        self.pwadHLayout = QtWidgets.QHBoxLayout()
        self.pwadHLayout.setSpacing(0)
        self.pwadHLayout.setObjectName("pwadHLayout")
        self.pwadLabel = QtWidgets.QLabel(self.layoutWidget)
        self.pwadLabel.setToolTip("<html><head/><body><p>Add external files to run here, such as custom maps and mods (known as PWADs or &quot;patch WADs&quot;). Common extensions include .wad, .pk3, .deh, and .bex. BDL can also accept .zip files.</p><p>Drag and drop files to reorder them. Uncheck files to prevent them from being loaded.</p><p><span style=\" font-weight:600;\">Files will be loaded in the order they are listed, top to bottom.</span></p><p>This means if multiple files replace the same data (i.e. MAP01), only the last instance of that data will be loaded. Keep this in mind, especially when loading music and cosmetic mods.</p></body></html>")
        self.pwadLabel.setText("External Files")
        self.pwadLabel.setObjectName("pwadLabel")
        self.pwadHLayout.addWidget(self.pwadLabel)
        spacerItem = QtWidgets.QSpacerItem(3, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.pwadHLayout.addItem(spacerItem)
        self.pwadAdd = QtWidgets.QPushButton(self.layoutWidget)
        self.pwadAdd.setMinimumSize(QtCore.QSize(15, 15))
        self.pwadAdd.setMaximumSize(QtCore.QSize(30, 15))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ui/plus2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pwadAdd.setIcon(icon1)
        self.pwadAdd.setIconSize(QtCore.QSize(9, 9))
        self.pwadAdd.setObjectName("pwadAdd")
        self.pwadHLayout.addWidget(self.pwadAdd)
        self.pwadRem = QtWidgets.QPushButton(self.layoutWidget)
        self.pwadRem.setMaximumSize(QtCore.QSize(15, 15))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ui/minus2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pwadRem.setIcon(icon2)
        self.pwadRem.setIconSize(QtCore.QSize(9, 9))
        self.pwadRem.setObjectName("pwadRem")
        self.pwadHLayout.addWidget(self.pwadRem)
        spacerItem1 = QtWidgets.QSpacerItem(3000, 0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.pwadHLayout.addItem(spacerItem1)
        self.leftVLayout.addLayout(self.pwadHLayout)
        self.pwadList = bdlListWidget(self.layoutWidget)
        self.pwadList.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.pwadList.setAcceptDrops(True)
        self.pwadList.setStyleSheet("QListWidget {\n"
"outline: 0; }\n"
"\n"
"QListWidget::indicator {\n"
"width: 8px;\n"
"height: 8px;\n"
"right: -4px; }\n"
"\n"
"QListView::item:text {\n"
"color: black;\n"
"padding-left: -5px;\n"
"padding-top: -1px; }\n"
"\n"
"QListWidget::indicator::checked { image: url(:/ui/checkbox_on6.png); }")
        self.pwadList.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.pwadList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pwadList.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.pwadList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.pwadList.setMovement(QtWidgets.QListView.Free)
        self.pwadList.setObjectName("pwadList")
        self.leftVLayout.addWidget(self.pwadList)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.rightVLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.rightVLayout.setContentsMargins(0, 0, 0, 0)
        self.rightVLayout.setSpacing(1)
        self.rightVLayout.setObjectName("rightVLayout")
        self.portHLayout = QtWidgets.QHBoxLayout()
        self.portHLayout.setSpacing(0)
        self.portHLayout.setObjectName("portHLayout")
        self.portLabel = QtWidgets.QLabel(self.layoutWidget_2)
        self.portLabel.setToolTip("<html><head/><body><p>Install new or add existing source ports here.</p><p>Source ports are ports of Doom\'s source code and are the basis through which all game data (WADs) are played.</p></body></html>")
        self.portLabel.setText("Source Port")
        self.portLabel.setObjectName("portLabel")
        self.portHLayout.addWidget(self.portLabel)
        spacerItem2 = QtWidgets.QSpacerItem(3, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.portHLayout.addItem(spacerItem2)
        self.portDownload = QtWidgets.QPushButton(self.layoutWidget_2)
        self.portDownload.setMaximumSize(QtCore.QSize(15, 15))
        self.portDownload.setToolTip("<html><head/><body><p>Download, install, and configure a new source port directly through BDL.</p></body></html>")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ui/download7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.portDownload.setIcon(icon3)
        self.portDownload.setIconSize(QtCore.QSize(9, 9))
        self.portDownload.setObjectName("portDownload")
        self.portHLayout.addWidget(self.portDownload)
        self.portMenuButton = QtWidgets.QToolButton(self.layoutWidget_2)
        self.portMenuButton.setMaximumSize(QtCore.QSize(15, 15))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ui/browse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.portMenuButton.setIcon(icon4)
        self.portMenuButton.setIconSize(QtCore.QSize(9, 9))
        self.portMenuButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.portMenuButton.setObjectName("portMenuButton")
        self.portHLayout.addWidget(self.portMenuButton)
        spacerItem3 = QtWidgets.QSpacerItem(3000, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.portHLayout.addItem(spacerItem3)
        self.rightVLayout.addLayout(self.portHLayout)
        self.portCombo = bdlComboBox(self.layoutWidget_2)
        self.portCombo.setAcceptDrops(True)
        self.portCombo.setObjectName("portCombo")
        self.rightVLayout.addWidget(self.portCombo)
        spacerItem4 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.rightVLayout.addItem(spacerItem4)
        self.iwadHLayout = QtWidgets.QHBoxLayout()
        self.iwadHLayout.setSpacing(0)
        self.iwadHLayout.setObjectName("iwadHLayout")
        self.iwadLabel = QtWidgets.QLabel(self.layoutWidget_2)
        self.iwadLabel.setToolTip("<html><head/><body><p>IWADs or &quot;Interal WADs&quot; are official game data, and act as the base for which custom files (or PWADs) replace and load custom data.</p><p>Examples of IWADs are <span style=\" font-style:italic;\">DOOM.WAD, DOOM2.WAD, TNT.WAD, PLUTONIA.WAD</span>, etc.</p></body></html>")
        self.iwadLabel.setText("IWAD")
        self.iwadLabel.setObjectName("iwadLabel")
        self.iwadHLayout.addWidget(self.iwadLabel)
        spacerItem5 = QtWidgets.QSpacerItem(3, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.iwadHLayout.addItem(spacerItem5)
        self.iwadAdd = QtWidgets.QPushButton(self.layoutWidget_2)
        self.iwadAdd.setMinimumSize(QtCore.QSize(15, 15))
        self.iwadAdd.setMaximumSize(QtCore.QSize(30, 15))
        self.iwadAdd.setIcon(icon1)
        self.iwadAdd.setIconSize(QtCore.QSize(9, 9))
        self.iwadAdd.setObjectName("iwadAdd")
        self.iwadHLayout.addWidget(self.iwadAdd)
        self.iwadRem = QtWidgets.QPushButton(self.layoutWidget_2)
        self.iwadRem.setMaximumSize(QtCore.QSize(15, 15))
        self.iwadRem.setIcon(icon2)
        self.iwadRem.setIconSize(QtCore.QSize(9, 9))
        self.iwadRem.setObjectName("iwadRem")
        self.iwadHLayout.addWidget(self.iwadRem)
        self.iwadMenuButton = QtWidgets.QToolButton(self.layoutWidget_2)
        self.iwadMenuButton.setMaximumSize(QtCore.QSize(15, 15))
        self.iwadMenuButton.setIcon(icon4)
        self.iwadMenuButton.setIconSize(QtCore.QSize(9, 9))
        self.iwadMenuButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.iwadMenuButton.setObjectName("iwadMenuButton")
        self.iwadHLayout.addWidget(self.iwadMenuButton)
        spacerItem6 = QtWidgets.QSpacerItem(3000, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.iwadHLayout.addItem(spacerItem6)
        self.rightVLayout.addLayout(self.iwadHLayout)
        self.iwadList = bdlListWidget(self.layoutWidget_2)
        self.iwadList.setAcceptDrops(True)
        self.iwadList.setStyleSheet("QListWidget { outline: 0; }\n"
"\n"
"QListWidget::item {\n"
"margin-top: -4px;\n"
"margin-bottom: 1px; }\n"
"\n"
"QListView::item::text { color: black; }\n"
"\n"
"QListView::item:selected {\n"
"background-color: rgb(230, 230, 230);\n"
"margin-top: 0px;\n"
"margin-bottom: 0px; }\n"
"\n"
"QListView::item:selected:active {\n"
"background-color: rgb(0, 122, 215);\n"
"color: white; }")
        self.iwadList.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.iwadList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.iwadList.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.iwadList.setMovement(QtWidgets.QListView.Free)
        self.iwadList.setObjectName("iwadList")
        self.rightVLayout.addWidget(self.iwadList)
        self.bottomGLayout.addWidget(self.splitter)
        self.parameterLineEdit = QtWidgets.QLineEdit(self.tabMain)
        self.parameterLineEdit.setToolTip("<html><head/><body><p>Add more command line arguments here, separated by spaces.</p></body></html>")
        self.parameterLineEdit.setPlaceholderText("Extra command line arguments")
        self.parameterLineEdit.setObjectName("parameterLineEdit")
        self.bottomGLayout.addWidget(self.parameterLineEdit)
        self.bottomHLayout = QtWidgets.QHBoxLayout()
        self.bottomHLayout.setSpacing(2)
        self.bottomHLayout.setObjectName("bottomHLayout")
        self.complevelCombo = QtWidgets.QComboBox(self.tabMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.complevelCombo.sizePolicy().hasHeightForWidth())
        self.complevelCombo.setSizePolicy(sizePolicy)
        self.complevelCombo.setMinimumSize(QtCore.QSize(128, 0))
        self.complevelCombo.setToolTip("<html><head/><body><p>Complevels, or compatibilty levels, are used by PrBoom+ and GLBoom+ to emulate various Doom versions and formats. This dropdown features the most common complevels.</p><p>If you\'re playing a custom wad, look for &quot;complevel&quot;, &quot;cl&quot;, a source port, or a specific format (vanilla, limit-removing, boom, MBF, UDMF) mentioned in its description, to know what to pick. If it says &quot;vanilla&quot; or &quot;limit-removing&quot; and its for Doom 2, pick complevel 2. If it says &quot;UDMF&quot; or &quot;Hexen in Doom 2&quot;, pick a ZDoom source port.</p><p>This dropdown can be overridden by manually specifying a complevel as one of your extra command line arguments.</p><p><span style=\" font-weight:600;\">This dropdown will be disabled if you\'re playing a demo.</span></p><p><span style=\" font-weight:600;\">This dropdown has no effect on other source ports.</span></p></body></html>")
        self.complevelCombo.setObjectName("complevelCombo")
        self.complevelCombo.addItem("")
        self.complevelCombo.setItemText(0, "-complevel 2 (Doom II)")
        self.complevelCombo.addItem("")
        self.complevelCombo.setItemText(1, "-complevel 3 (Ultimate Doom)")
        self.complevelCombo.addItem("")
        self.complevelCombo.setItemText(2, "-complevel 4 (Final Doom)")
        self.complevelCombo.addItem("")
        self.complevelCombo.setItemText(3, "-complevel 9 (Boom)")
        self.complevelCombo.addItem("")
        self.complevelCombo.setItemText(4, "-complevel 11 (MBF)")
        self.bottomHLayout.addWidget(self.complevelCombo)
        self.launchButton = QtWidgets.QPushButton(self.tabMain)
        self.launchButton.setMinimumSize(QtCore.QSize(50, 22))
        self.launchButton.setMaximumSize(QtCore.QSize(50, 22))
        self.launchButton.setText("Launch")
        self.launchButton.setDefault(True)
        self.launchButton.setObjectName("launchButton")
        self.bottomHLayout.addWidget(self.launchButton)
        self.bottomGLayout.addLayout(self.bottomHLayout)
        self.tabMainGLayout.addLayout(self.bottomGLayout, 0, 0, 1, 2)
        self.gridLayout.addLayout(self.tabMainGLayout, 7, 0, 1, 2)
        self.tabWidget.addTab(self.tabMain, "Main")
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabSettings)
        self.gridLayout_4.setContentsMargins(-1, 15, 12, 11)
        self.gridLayout_4.setVerticalSpacing(4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.demoGroup = QtWidgets.QGroupBox(self.tabSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demoGroup.sizePolicy().hasHeightForWidth())
        self.demoGroup.setSizePolicy(sizePolicy)
        self.demoGroup.setMinimumSize(QtCore.QSize(0, 56))
        self.demoGroup.setToolTip("")
        self.demoGroup.setTitle("Record/Play Demo")
        self.demoGroup.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.demoGroup.setFlat(False)
        self.demoGroup.setCheckable(True)
        self.demoGroup.setChecked(False)
        self.demoGroup.setObjectName("demoGroup")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.demoGroup)
        self.gridLayout_9.setContentsMargins(-1, 2, -1, 6)
        self.gridLayout_9.setHorizontalSpacing(1)
        self.gridLayout_9.setVerticalSpacing(4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.demoPlayRadio = QtWidgets.QRadioButton(self.demoGroup)
        self.demoPlayRadio.setText("Play")
        self.demoPlayRadio.setObjectName("demoPlayRadio")
        self.gridLayout_9.addWidget(self.demoPlayRadio, 1, 0, 1, 1)
        self.demoPlayBrowseButton = QtWidgets.QPushButton(self.demoGroup)
        self.demoPlayBrowseButton.setMaximumSize(QtCore.QSize(22, 22))
        self.demoPlayBrowseButton.setText("...")
        self.demoPlayBrowseButton.setObjectName("demoPlayBrowseButton")
        self.gridLayout_9.addWidget(self.demoPlayBrowseButton, 1, 2, 1, 1)
        self.demoRecordNameLineEdit = QtWidgets.QLineEdit(self.demoGroup)
        self.demoRecordNameLineEdit.setPlaceholderText("Name of demo")
        self.demoRecordNameLineEdit.setObjectName("demoRecordNameLineEdit")
        self.gridLayout_9.addWidget(self.demoRecordNameLineEdit, 0, 1, 1, 2)
        self.demoPlayPathLineEdit = QtWidgets.QLineEdit(self.demoGroup)
        self.demoPlayPathLineEdit.setPlaceholderText("Path to demo")
        self.demoPlayPathLineEdit.setObjectName("demoPlayPathLineEdit")
        self.gridLayout_9.addWidget(self.demoPlayPathLineEdit, 1, 1, 1, 1)
        self.demoRecordRadio = QtWidgets.QRadioButton(self.demoGroup)
        self.demoRecordRadio.setText("Record")
        self.demoRecordRadio.setChecked(True)
        self.demoRecordRadio.setObjectName("demoRecordRadio")
        self.gridLayout_9.addWidget(self.demoRecordRadio, 0, 0, 1, 1)
        self.demoAutoRecordCheck = QtWidgets.QCheckBox(self.demoGroup)
        self.demoAutoRecordCheck.setToolTip("<html><head/><body><p>Automatically start recording a new demo after the previous recording finishes. Mainly intended for speedrunners, who must restart frequently.</p><p>Appends an attempt number to the end of each file. Demos must be deleted manually.</p><p><span style=\" font-weight:600;\">This setting must be turned off while in-game</span></p></body></html>")
        self.demoAutoRecordCheck.setText("Auto-record new demos")
        self.demoAutoRecordCheck.setObjectName("demoAutoRecordCheck")
        self.gridLayout_9.addWidget(self.demoAutoRecordCheck, 2, 0, 1, 3)
        self.gridLayout_4.addWidget(self.demoGroup, 0, 0, 1, 1)
        self.warpGroup = QtWidgets.QGroupBox(self.tabSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warpGroup.sizePolicy().hasHeightForWidth())
        self.warpGroup.setSizePolicy(sizePolicy)
        self.warpGroup.setMinimumSize(QtCore.QSize(0, 56))
        self.warpGroup.setTitle("Warp to level")
        self.warpGroup.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.warpGroup.setFlat(False)
        self.warpGroup.setCheckable(True)
        self.warpGroup.setChecked(False)
        self.warpGroup.setObjectName("warpGroup")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.warpGroup)
        self.gridLayout_10.setContentsMargins(-1, 2, -1, 6)
        self.gridLayout_10.setVerticalSpacing(4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.warpMapLabel = QtWidgets.QLabel(self.warpGroup)
        self.warpMapLabel.setText("Map")
        self.warpMapLabel.setObjectName("warpMapLabel")
        self.gridLayout_10.addWidget(self.warpMapLabel, 0, 0, 1, 1)
        self.warpMapCombo = QtWidgets.QComboBox(self.warpGroup)
        self.warpMapCombo.setObjectName("warpMapCombo")
        self.warpMapCombo.addItem("")
        self.warpMapCombo.setItemText(0, "")
        self.gridLayout_10.addWidget(self.warpMapCombo, 0, 1, 1, 1)
        self.warpSkillLabel_2 = QtWidgets.QLabel(self.warpGroup)
        self.warpSkillLabel_2.setText("Skill")
        self.warpSkillLabel_2.setObjectName("warpSkillLabel_2")
        self.gridLayout_10.addWidget(self.warpSkillLabel_2, 1, 0, 1, 1)
        self.warpSkillCombo = QtWidgets.QComboBox(self.warpGroup)
        self.warpSkillCombo.setObjectName("warpSkillCombo")
        self.warpSkillCombo.addItem("")
        self.warpSkillCombo.setItemText(0, "I\'m Too Young To Die")
        self.warpSkillCombo.addItem("")
        self.warpSkillCombo.setItemText(1, "Hey, Not Too Rough")
        self.warpSkillCombo.addItem("")
        self.warpSkillCombo.setItemText(2, "Hurt Me Plenty")
        self.warpSkillCombo.addItem("")
        self.warpSkillCombo.setItemText(3, "Ultra-Violence")
        self.warpSkillCombo.addItem("")
        self.warpSkillCombo.setItemText(4, "NIGHTMARE!")
        self.gridLayout_10.addWidget(self.warpSkillCombo, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.warpGroup, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabSettings, "Settings")
        self.tabTools = QtWidgets.QWidget()
        self.tabTools.setObjectName("tabTools")
        self.tabWidget.addTab(self.tabTools, "Tools")
        self.tabInstall = QtWidgets.QWidget()
        self.tabInstall.setObjectName("tabInstall")
        self.tabWidget.addTab(self.tabInstall, "Install")
        self.tabBDL = QtWidgets.QWidget()
        self.tabBDL.setObjectName("tabBDL")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabBDL)
        self.gridLayout_6.setContentsMargins(0, 15, 0, 12)
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.commandLinePreviewButton = QtWidgets.QPushButton(self.tabBDL)
        self.commandLinePreviewButton.setMaximumSize(QtCore.QSize(126, 16777215))
        self.commandLinePreviewButton.setText("Preview Command Line")
        self.commandLinePreviewButton.setObjectName("commandLinePreviewButton")
        self.gridLayout_6.addWidget(self.commandLinePreviewButton, 3, 1, 1, 1)
        self.aboutButton = QtWidgets.QPushButton(self.tabBDL)
        self.aboutButton.setMaximumSize(QtCore.QSize(46, 21))
        self.aboutButton.setText("About")
        self.aboutButton.setObjectName("aboutButton")
        self.gridLayout_6.addWidget(self.aboutButton, 3, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(2)
        self.formLayout.setObjectName("formLayout")
        self.bdlAutoClose = QtWidgets.QCheckBox(self.tabBDL)
        self.bdlAutoClose.setToolTip("Close BDL after launching a game. BDL\n"
"will only close once the game is closed.")
        self.bdlAutoClose.setText("Close on launch")
        self.bdlAutoClose.setObjectName("bdlAutoClose")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.bdlAutoClose)
        self.bdlForceCaps = QtWidgets.QCheckBox(self.tabBDL)
        self.bdlForceCaps.setToolTip("Force the word \"Doom\" to be automatically\n"
"capitalized in the selected style for all currently\n"
"added and any future added IWADs.")
        self.bdlForceCaps.setText("Force capitalization:")
        self.bdlForceCaps.setChecked(True)
        self.bdlForceCaps.setObjectName("bdlForceCaps")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.bdlForceCaps)
        self.bdlForceCapsPreferenceCombo = QtWidgets.QComboBox(self.tabBDL)
        self.bdlForceCapsPreferenceCombo.setMaximumSize(QtCore.QSize(55, 17))
        self.bdlForceCapsPreferenceCombo.setCurrentText("Doom")
        self.bdlForceCapsPreferenceCombo.setObjectName("bdlForceCapsPreferenceCombo")
        self.bdlForceCapsPreferenceCombo.addItem("")
        self.bdlForceCapsPreferenceCombo.setItemText(0, "Doom")
        self.bdlForceCapsPreferenceCombo.addItem("")
        self.bdlForceCapsPreferenceCombo.setItemText(1, "DOOM")
        self.bdlForceCapsPreferenceCombo.addItem("")
        self.bdlForceCapsPreferenceCombo.setItemText(2, "DooM")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bdlForceCapsPreferenceCombo)
        self.bdlAutoDetectIWADs = QtWidgets.QCheckBox(self.tabBDL)
        self.bdlAutoDetectIWADs.setToolTip("Generates and reads the md5 hashes\n"
"of IWADs to validate and name them.\n"
"\n"
"May cause minor hiccups when adding\n"
"IWADs on older machines.")
        self.bdlAutoDetectIWADs.setText("Automatically detect IWADs")
        self.bdlAutoDetectIWADs.setChecked(True)
        self.bdlAutoDetectIWADs.setObjectName("bdlAutoDetectIWADs")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.bdlAutoDetectIWADs)
        self.gridLayout_6.addLayout(self.formLayout, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tabBDL, "bdl")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        BDLMainWindow.setCentralWidget(self.centralwidget)
        #self.menuBar = QtWidgets.QMenuBar(BDLMainWindow)
        #self.menuBar.setGeometry(QtCore.QRect(0, 0, 225, 21))
        #self.menuBar.setObjectName("menuBar")
        self.portMenu = QtWidgets.QMenu(None)
        self.portMenu.setTitle("Source Ports")
        self.portMenu.setObjectName("portMenu")
        self.iwadMenu = QtWidgets.QMenu(None)
        self.iwadMenu.setTitle("IWADs")
        self.iwadMenu.setObjectName("iwadMenu")
        self.iwadMenuSteam = QtWidgets.QMenu(self.iwadMenu)
        self.iwadMenuSteam.setTitle("Purchase on Steam...")
        self.iwadMenuSteam.setObjectName("iwadMenuSteam")
        self.iwadMenuDeals = QtWidgets.QMenu(self.iwadMenu)
        self.iwadMenuDeals.setTitle("Check for deals...")
        self.iwadMenuDeals.setObjectName("iwadMenuDeals")
        #BDLMainWindow.setMenuBar(self.menuBar)
        self.portAdd = QtWidgets.QAction(BDLMainWindow)
        self.portAdd.setText("Add existing source ports")
        self.portAdd.setObjectName("portAdd")
        self.portRem = QtWidgets.QAction(BDLMainWindow)
        self.portRem.setText("Remove selected source port")
        self.portRem.setObjectName("portRem")
        self.portMoveDown = QtWidgets.QAction(BDLMainWindow)
        self.portMoveDown.setText("Move down")
        self.portMoveDown.setObjectName("portMoveDown")
        self.portMoveUp = QtWidgets.QAction(BDLMainWindow)
        self.portMoveUp.setText("Move up")
        self.portMoveUp.setObjectName("portMoveUp")
        self.portDownloadAction = QtWidgets.QAction(BDLMainWindow)
        self.portDownloadAction.setText("Download new source port")
        self.portDownloadAction.setObjectName("portDownloadAction")
        self.portMoveToBottom = QtWidgets.QAction(BDLMainWindow)
        self.portMoveToBottom.setText("Move to bottom")
        self.portMoveToBottom.setObjectName("portMoveToBottom")
        self.portMoveToTop = QtWidgets.QAction(BDLMainWindow)
        self.portMoveToTop.setText("Move to top")
        self.portMoveToTop.setObjectName("portMoveToTop")
        self.portRename = QtWidgets.QAction(BDLMainWindow)
        self.portRename.setText("Rename selected source port")
        self.portRename.setObjectName("portRename")
        self.portBrowseLocalFiles = QtWidgets.QAction(BDLMainWindow)
        self.portBrowseLocalFiles.setText("Open source port location")
        self.portBrowseLocalFiles.setObjectName("portBrowseLocalFiles")
        self.iwadBrowseLocalFiles = QtWidgets.QAction(BDLMainWindow)
        self.iwadBrowseLocalFiles.setText("Open IWAD location")
        self.iwadBrowseLocalFiles.setObjectName("iwadBrowseLocalFiles")
        self.iwadSteamUDoom = QtWidgets.QAction(BDLMainWindow)
        self.iwadSteamUDoom.setText("Ultimate Doom")
        self.iwadSteamUDoom.setObjectName("iwadSteamUDoom")
        self.iwadSteamDoom2 = QtWidgets.QAction(BDLMainWindow)
        self.iwadSteamDoom2.setText("Doom II: Hell on Earth")
        self.iwadSteamDoom2.setObjectName("iwadSteamDoom2")
        self.iwadSteamFinalDoom = QtWidgets.QAction(BDLMainWindow)
        self.iwadSteamFinalDoom.setText("Final Doom")
        self.iwadSteamFinalDoom.setObjectName("iwadSteamFinalDoom")
        self.iwadSteamClassicComplete = QtWidgets.QAction(BDLMainWindow)
        self.iwadSteamClassicComplete.setText("Doom Classic Complete")
        self.iwadSteamClassicComplete.setObjectName("iwadSteamClassicComplete")
        self.iwadDealsUDoom = QtWidgets.QAction(BDLMainWindow)
        self.iwadDealsUDoom.setText("Ultimate Doom")
        self.iwadDealsUDoom.setObjectName("iwadDealsUDoom")
        self.iwadDealsDoom2 = QtWidgets.QAction(BDLMainWindow)
        self.iwadDealsDoom2.setText("Doom II: Hell on Earth")
        self.iwadDealsDoom2.setObjectName("iwadDealsDoom2")
        self.iwadDealsFinalDoom = QtWidgets.QAction(BDLMainWindow)
        self.iwadDealsFinalDoom.setText("Final Doom")
        self.iwadDealsFinalDoom.setObjectName("iwadDealsFinalDoom")
        self.iwadDealsClassicComplete = QtWidgets.QAction(BDLMainWindow)
        self.iwadDealsClassicComplete.setText("Doom Classic Complete")
        self.iwadDealsClassicComplete.setObjectName("iwadDealsClassicComplete")
        self.portMenu.addAction(self.portDownloadAction)
        self.portMenu.addSeparator()
        self.portMenu.addAction(self.portAdd)
        self.portMenu.addAction(self.portRem)
        self.portMenu.addSeparator()
        self.portMenu.addAction(self.portRename)
        self.portMenu.addAction(self.portBrowseLocalFiles)
        self.portMenu.addSeparator()
        self.portMenu.addAction(self.portMoveUp)
        self.portMenu.addAction(self.portMoveDown)
        self.portMenu.addAction(self.portMoveToBottom)
        self.portMenu.addAction(self.portMoveToTop)
        self.iwadMenuSteam.addAction(self.iwadSteamUDoom)
        self.iwadMenuSteam.addAction(self.iwadSteamDoom2)
        self.iwadMenuSteam.addAction(self.iwadSteamFinalDoom)
        self.iwadMenuSteam.addAction(self.iwadSteamClassicComplete)
        self.iwadMenuDeals.addAction(self.iwadDealsUDoom)
        self.iwadMenuDeals.addAction(self.iwadDealsDoom2)
        self.iwadMenuDeals.addAction(self.iwadDealsFinalDoom)
        self.iwadMenuDeals.addAction(self.iwadDealsClassicComplete)
        self.iwadMenu.addAction(self.iwadBrowseLocalFiles)
        self.iwadMenu.addSeparator()
        self.iwadMenu.addAction(self.iwadMenuSteam.menuAction())
        self.iwadMenu.addAction(self.iwadMenuDeals.menuAction())
        #self.menuBar.addAction(self.portMenu.menuAction())
        #self.menuBar.addAction(self.iwadMenu.menuAction())

        self.tabWidget.setCurrentIndex(0)
        self.warpSkillCombo.setCurrentIndex(3)
        self.demoGroup.toggled['bool'].connect(self.warpGroup.setChecked)
        QtCore.QMetaObject.connectSlotsByName(BDLMainWindow)






        self.complevelCombo.setItemData(0, "-complevel 2", 3)
        self.complevelCombo.setItemData(1, "-complevel 3", 3)
        self.complevelCombo.setItemData(2, "-complevel 4", 3)
        self.complevelCombo.setItemData(3, "-complevel 9", 3)
        self.complevelCombo.setItemData(4, "-complevel 11", 3)

        self.launchButton.clicked.connect(self.prepareLaunch)
        self.aboutButton.clicked.connect(self.openAboutDialog)

        self.pwadAdd.clicked.connect(lambda: self.prepareAddFile(self.pwadList))
        self.pwadRem.clicked.connect(lambda: self.removeListItem(self.pwadList))

        self.iwadMenuButton.setMenu(self.iwadMenu)
        self.iwadList.itemDoubleClicked.connect(self.resetFlags)
        self.iwadAdd.clicked.connect(lambda: self.prepareAddFile(self.iwadList))
        self.iwadRem.clicked.connect(lambda: self.removeListItem(self.iwadList))

        self.iwadSteamUDoom.triggered.connect(lambda: webbrowser.open('https://store.steampowered.com/app/2280/Ultimate_Doom/'))
        self.iwadSteamDoom2.triggered.connect(lambda: webbrowser.open('https://store.steampowered.com/app/2300/DOOM_II/'))
        self.iwadSteamFinalDoom.triggered.connect(lambda: webbrowser.open('https://store.steampowered.com/app/2290/Final_DOOM/'))
        self.iwadSteamClassicComplete.triggered.connect(lambda: webbrowser.open('https://store.steampowered.com/sub/18397/'))
        self.iwadDealsUDoom.triggered.connect(lambda: webbrowser.open('https://isthereanydeal.com/game/ultimatedoom/info/'))
        self.iwadDealsDoom2.triggered.connect(lambda: webbrowser.open('https://isthereanydeal.com/game/doomii/info/'))
        self.iwadDealsFinalDoom.triggered.connect(lambda: webbrowser.open('https://isthereanydeal.com/game/finaldoom/info/'))
        self.iwadDealsClassicComplete.triggered.connect(lambda: webbrowser.open('https://isthereanydeal.com/game/doomclassiccomplete/info/'))


        self.portMenuButton.setMenu(self.portMenu)
        self.portAdd.triggered.connect(lambda: self.prepareAddFile(self.portCombo))
        self.portRem.triggered.connect(lambda: self.portCombo.removeItem(self.portCombo.currentIndex()))

        self.commandLinePreviewButton.clicked.connect(lambda: run.showPopup(title="Command line preview",
                                                                            text=self.prepareLaunch(noLaunch=True),
                                                                            icon=QtWidgets.QMessageBox.Information))

        # Default values for properties to be loaded from the config.
        self.lastDir = '.'
        self.autoClose = False

        self.loadConfig()





    def firstTimeSetup(self):
        # TODO: also check updates
        if os.path.exists("%APPDATA%\\Vectec Software\\qZDL.ini"):
            pass        # TODO: s t e a l ZDL's config
        else:
            run.findSteamIWADs(self.iwadList)

        config = configparser.ConfigParser()
        config['bdl.general'] = {'lastdir':'.',
                                 'autoclose':'false',
                                 'windowsize':'225,247',
                                 'windowpos':'350,250'}



    def loadConfig(self):
        if not os.path.exists("bdl.ini"):
            self.firstTimeSetup()
        else:
            config = configparser.ConfigParser()
            config.read("bdl.ini")

            # set window size/pos, splitter sizes, other settings
            if 'bdl.general' in config:
                windowSizeX, windowSizeY = config['bdl.general'].get('windowsize',fallback='225,247').split(",")
                BDLMainWindow.resize(int(windowSizeX), int(windowSizeY))
                windowPosX, windowPosY = config['bdl.general'].get('windowpos',fallback='350,250').split(",")
                BDLMainWindow.move(int(windowPosX), int(windowPosY))

                self.lastDir = config['bdl.general'].get('lastdir', fallback='.')
                self.autoClose = config['bdl.general'].getboolean('autoclose', fallback='false')
                try: self.splitter.setSizes(list(int(size) for size in config['bdl.general'].get('lastsplittersize').split(',')))
                except: pass

            # load saved pwads/iwads/ports
            if 'bdl.iwads' in config:
                index = 0
                while config['bdl.iwads'].get(f'iwadpath{index}'):
                    try:
                        run.addFileFromConfig(self.iwadList,
                                              path=config['bdl.iwads'].get(f'iwadpath{index}'),
                                              name=config['bdl.iwads'].get(f'iwadname{index}'))  # TODO: fallback?
                    except:
                        print("iwad:",sys.exc_info()[0])   # TODO: clean up error stuff here
                    index+=1
            if 'bdl.pwads' in config:
                index = 0
                while config['bdl.pwads'].get(f'pwadpath{index}'):
                    try:
                        run.addFileFromConfig(self.pwadList,
                                              path=config['bdl.pwads'].get(f'pwadpath{index}'),
                                              name=None,
                                              checked=config['bdl.pwads'].getboolean(f'pwadchecked{index}'))
                    except:
                        print("pwad:",sys.exc_info()[0])
                    index+=1
            if 'bdl.ports' in config:
                index = 0
                while config['bdl.ports'].get(f'portpath{index}'):
                    try:
                        run.addFileFromConfig(self.portCombo,
                                              path=config['bdl.ports'].get(f'portpath{index}'),
                                              name=config['bdl.ports'].get(f'portname{index}'))
                    except:
                        print("port:",sys.exc_info()[0])
                    index+=1
            # load saved parameters and selections
            if 'bdl.save' in config:
                save = config['bdl.save']
                self.parameterLineEdit.setText(save.get('extra', ''))
                self.portCombo.setCurrentIndex(save.getint('portindex', fallback=0))
                self.iwadList.setCurrentRow(save.getint('iwadindex', fallback=0))
                self.complevelCombo.setCurrentIndex(save.getint('complevelindex', fallback=0))





    def saveConfig(self):       # TODO: add md5 check here? might not save time
        config = configparser.ConfigParser()
        config['bdl.general'] = {}
        general = config['bdl.general']
        general['lastdir'] = self.lastDir
        general['autoclose'] = str(self.autoClose)
        general['windowpos'] = str(BDLMainWindow.x()-1) + ',' + str(BDLMainWindow.y()-31)   # -1 and -31 due to unknown offset
        general['windowsize'] = str(self.centralwidget.frameGeometry().width()) + ',' + str(self.centralwidget.frameGeometry().height())
        general['lastsplittersize'] = ','.join(str(size) for size in self.splitter.sizes())

        config['bdl.save'] = {}
        save = config['bdl.save']
        save['extra'] = self.parameterLineEdit.text()
        save['portindex'] = str(self.portCombo.currentIndex())
        save['iwadindex'] = str(self.iwadList.currentRow())
        save['complevelindex'] = str(self.complevelCombo.currentIndex())
        save['demoenabled'] = ''
        save['demorecord'] = ''
        save['demorecordname'] = ''
        save['demoplay'] = ''
        save['demoplaypath'] = ''
        save['warpenabled'] = ''
        save['warp'] = ''
        save['skill'] = ''

        # loop through file widgets and save all wads/ports and their properties
        config['bdl.iwads'] = {}
        config['bdl.pwads'] = {}
        config['bdl.ports'] = {}
        for i in range(self.iwadList.count()):
            iwad = self.iwadList.item(i)
            config['bdl.iwads'][f'iwadname{i}'] = iwad.text()
            config['bdl.iwads'][f'iwadpath{i}'] = iwad.data(3)
        for i in range(self.pwadList.count()):
            pwad = self.pwadList.item(i)
            config['bdl.pwads'][f'pwadchecked{i}'] = 'True' if pwad.checkState() == 2 else 'False'
            config['bdl.pwads'][f'pwadpath{i}'] = pwad.data(3)
        for i in range(self.portCombo.count()):
            config['bdl.ports'][f'portname{i}'] = self.portCombo.itemText(i)
            config['bdl.ports'][f'portpath{i}'] = self.portCombo.itemData(i,3)
        with open('bdl.ini', 'w') as ini:
            config.write(ini)





    def prepareLaunch(self, noLaunch=False):
        # TODO: add relative path variant?
        activePWADs = ""
        activeDEH = ""
        for i in range(self.pwadList.count()):
            pwad = self.pwadList.item(i)
            if pwad.checkState() == 2:                  # 2 -> item is checked
                filePath = pwad.data(3)
                if filePath.endswith("deh") or filePath.endswith("bex"):
                    activeDEH += os.path.abspath(filePath) + " "     # '"' is just " as a string
                else:
                    activePWADs += os.path.abspath(filePath) + " "
        try:
            commandLine = run.run(port=self.portCombo.currentData(3),
                                  iwad=self.iwadList.currentItem().data(3),
                                  complevel=self.complevelCombo.currentData(3) if self.complevelCombo.isEnabled() else None,
                                  pwads=activePWADs,        # TODO: ^^^ if demo is going to play, complevel dropdown is disabled
                                  deh=activeDEH,
                                  warp=0,
                                  skill=0,
                                  extra=self.parameterLineEdit.text(),
                                  noLaunch=noLaunch)
            if noLaunch: return commandLine
            elif self.autoClose: BDLMainWindow.close()      # important!!! -> only closes AFTER game is closed

        # TODO: add custom doom warning icons, move warning explanation elsewhere?
        except AttributeError as e:      # AttributeError means no IWAD -> NoneType.data(3) causes it
            print(e)        # TODO: add logger
            if self.portCombo.currentData(3) is None:       # Checks to see if there's no port -> double whammy
                run.showPopup(title="Missing source port and IWAD!",
                                    text="No source port or IWAD detected! Both a source port\n"
                                    "and a valid IWAD are required to run Doom games.",
                                    textInformative=("Source ports are ports of Doom's original source\n"
                                                     "code, and are used to run game data.\n"
                                                     "Examples: PrBoom+, GZDoom, Chocolate Doom\n\n"
                                                     "IWADs are official game data files. They contain all of the\n"
                                                     "game's assets, and are used as the base for custom wads.\n"
                                                     "Examples: DOOM.WAD, DOOM2.WAD, TNT.WAD, etc."))
            else:       # Port detected, just missing iwad.
                run.showPopup(title="Missing IWAD!",
                                    text="No IWAD detected! Both a source port and a\n"
                                    "valid IWAD are required to run Doom games.",
                                    textInformative=("Source ports are ports of Doom's original source\n"
                                                     "code, and are used to run game data.\n"
                                                     "Examples: PrBoom+, GZDoom, Chocolate Doom\n\n"
                                                     "IWADs are official game data files. They contain all of the\n"
                                                     "game's assets, and are used as the base for custom wads.\n"
                                                     "Examples: DOOM.WAD, DOOM2.WAD, TNT.WAD, etc."))
        except TypeError as e:       # TypeError means no port -> '"' + NoneType + '"' in run.run() causes it
            run.showPopup(title="Missing source port!",
                                text="No source port detected! Both a source port and\n"
                                "a valid IWAD are required to run Doom games.",
                                textInformative=("Source ports are ports of Doom's original source\n"
                                                 "code, and are used to run game data.\n"
                                                 "Examples: PrBoom+, GZDoom, Chocolate Doom\n\n"
                                                 "IWADs are official game data files. They contain all of the\n"
                                                 "game's assets, and are used as the base for custom wads.\n"
                                                 "Examples: DOOM.WAD, DOOM2.WAD, TNT.WAD, etc."))





    def resetFlags(self):       # Workaround for Qt bug in which dragged list items have their flags reset.
        try:
            self.iwadList.currentItem().setFlags(QtCore.Qt.ItemIsSelectable|
                                                 QtCore.Qt.ItemIsEditable|
                                                 QtCore.Qt.ItemIsDragEnabled|
                                                 QtCore.Qt.ItemIsEnabled)
        except: pass            # Try-except block to prevent crash when launching with no iwads

    def removeListItem(self, qlist):
        selected = list(qlist.row(item) for item in qlist.selectedItems())      # generates list of currently selected item indexes
        selected.sort(reverse=True)                     # sorts list to delete higher indexes first to avoid indexes being updated
        for index in selected:          # uses takeItem() to remove items and deletes them manually since qt won't do it for you
            garbage = qlist.takeItem(index)
            del garbage

    def prepareAddFile(self, widget):
        self.lastDir = run.addFile(widget, lastDir=self.lastDir)

    def openAboutDialog(self):
        aboutDialog = QtWidgets.QDialog()
        ui = window_about.Ui_aboutDialog()
        ui.setupUi(aboutDialog)
        aboutDialog.exec()


from bdlComboBox import bdlComboBox
from bdlListWidget import bdlListWidget
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BDLMainWindow = QtWidgets.QMainWindow()
    ui = Ui_BDLMainWindow()
    ui.setupUi(BDLMainWindow)
    BDLMainWindow.show()
    sys.exit(app.exec_())
