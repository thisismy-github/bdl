# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\res\window_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import window_about, run
import os, hashlib, configparser, subprocess, webbrowser

class Ui_BDLMainWindow(object):
    def setupUi(self, BDLMainWindow):
        BDLMainWindow.setObjectName("BDLMainWindow")
        BDLMainWindow.resize(193, 178)
        BDLMainWindow.setMinimumSize(QtCore.QSize(193, 178))
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
        spacerItem1 = QtWidgets.QSpacerItem(2666, 0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.pwadHLayout.addItem(spacerItem1)
        self.leftVLayout.addLayout(self.pwadHLayout)
        self.pwadList = bdlListWidget(self.layoutWidget)
        self.pwadList.setMinimumSize(QtCore.QSize(0, 64))
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
        spacerItem3 = QtWidgets.QSpacerItem(2666, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.portHLayout.addItem(spacerItem3)
        self.rightVLayout.addLayout(self.portHLayout)
        self.portCombo = bdlComboBox(self.layoutWidget_2)
        self.portCombo.setAcceptDrops(True)
        self.portCombo.setObjectName("portCombo")
        self.rightVLayout.addWidget(self.portCombo)
        self.portRenameLineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.portRenameLineEdit.setText("")
        self.portRenameLineEdit.setPlaceholderText("Enter new name")
        self.portRenameLineEdit.setObjectName("portRenameLineEdit")
        self.rightVLayout.addWidget(self.portRenameLineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(0, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.rightVLayout.addItem(spacerItem4)
        self.iwadHLayout = QtWidgets.QHBoxLayout()
        self.iwadHLayout.setSpacing(0)
        self.iwadHLayout.setObjectName("iwadHLayout")
        self.iwadLabel = QtWidgets.QLabel(self.layoutWidget_2)
        self.iwadLabel.setToolTip("<html><head/><body><p>IWADs or &quot;Interal WADs&quot; are official game data, and act as the base for which custom files (or PWADs) replace and load custom data.</p><p>Examples of IWADs are <span style=\" font-style:italic;\">DOOM.WAD, DOOM2.WAD, TNT.WAD, PLUTONIA.WAD</span>, etc.</p></body></html>")
        self.iwadLabel.setText("IWAD")
        self.iwadLabel.setObjectName("iwadLabel")
        self.iwadHLayout.addWidget(self.iwadLabel)
        spacerItem5 = QtWidgets.QSpacerItem(1, 13, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
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
        spacerItem6 = QtWidgets.QSpacerItem(2666, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.iwadHLayout.addItem(spacerItem6)
        self.rightVLayout.addLayout(self.iwadHLayout)
        self.iwadList = bdlListWidget(self.layoutWidget_2)
        self.iwadList.setMinimumSize(QtCore.QSize(0, 40))
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
        self.complevelCombo.setToolTip("<html><head/><body><p>Complevels, or compatibilty levels, are used by PrBoom+ and GLBoom+ to emulate various Doom versions and formats. This dropdown features the most common complevels.</p><p>If you\'re playing a custom wad, look for &quot;complevel&quot;, &quot;cl&quot;, a source port, or a specific format (vanilla, limit-removing, boom, MBF, UDMF) mentioned in its description, to know what to pick. If it says &quot;vanilla&quot; or &quot;limit-removing&quot; and its for Doom 2, pick complevel 2. If it says &quot;UDMF&quot; or &quot;Hexen in Doom 2&quot;, pick a ZDoom source port.</p><p>This dropdown can be overridden by manually specifying a complevel as one of your extra command line arguments.</p><p><span style=\" font-weight:600;\">This dropdown will have no effect if you\'re playing a demo.</span></p><p><span style=\" font-weight:600;\">This dropdown has no effect on other source ports.</span></p></body></html>")
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
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.tabSettings)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 183, 134))
        self.scrollAreaWidgetContents_3.setMinimumSize(QtCore.QSize(124, 0))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_11.setContentsMargins(0, 4, 0, 4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(-1, -1, -1, 3)
        self.gridLayout_8.setVerticalSpacing(4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.warpGroup = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warpGroup.sizePolicy().hasHeightForWidth())
        self.warpGroup.setSizePolicy(sizePolicy)
        self.warpGroup.setMinimumSize(QtCore.QSize(130, 0))
        self.warpGroup.setMaximumSize(QtCore.QSize(16777215, 13))
        self.warpGroup.setTitle("Warp to level")
        self.warpGroup.setCheckable(True)
        self.warpGroup.setChecked(False)
        self.warpGroup.setObjectName("warpGroup")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.warpGroup)
        self.gridLayout_10.setContentsMargins(7, 5, -1, 8)
        self.gridLayout_10.setVerticalSpacing(3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.warpSkillLabel = QtWidgets.QLabel(self.warpGroup)
        self.warpSkillLabel.setMaximumSize(QtCore.QSize(20, 16777215))
        self.warpSkillLabel.setText("Skill")
        self.warpSkillLabel.setObjectName("warpSkillLabel")
        self.gridLayout_10.addWidget(self.warpSkillLabel, 1, 0, 1, 1)
        self.warpMapLabel = QtWidgets.QLabel(self.warpGroup)
        self.warpMapLabel.setMaximumSize(QtCore.QSize(20, 16777215))
        self.warpMapLabel.setText("Map")
        self.warpMapLabel.setObjectName("warpMapLabel")
        self.gridLayout_10.addWidget(self.warpMapLabel, 0, 0, 1, 1)
        self.warpMapCombo = QtWidgets.QComboBox(self.warpGroup)
        self.warpMapCombo.setMinimumSize(QtCore.QSize(124, 0))
        self.warpMapCombo.setObjectName("warpMapCombo")
        self.warpMapCombo.addItem("")
        self.warpMapCombo.setItemText(0, "")
        self.gridLayout_10.addWidget(self.warpMapCombo, 0, 1, 1, 1)
        self.warpSkillCombo = QtWidgets.QComboBox(self.warpGroup)
        self.warpSkillCombo.setMinimumSize(QtCore.QSize(124, 0))
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
        self.gridLayout_8.addWidget(self.warpGroup, 1, 0, 1, 1)
        self.demoGroup = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demoGroup.sizePolicy().hasHeightForWidth())
        self.demoGroup.setSizePolicy(sizePolicy)
        self.demoGroup.setMinimumSize(QtCore.QSize(130, 0))
        self.demoGroup.setMaximumSize(QtCore.QSize(16777215, 13))
        self.demoGroup.setToolTip("")
        self.demoGroup.setTitle("Record/Play Demo")
        self.demoGroup.setFlat(False)
        self.demoGroup.setCheckable(True)
        self.demoGroup.setChecked(False)
        self.demoGroup.setObjectName("demoGroup")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.demoGroup)
        self.gridLayout_9.setContentsMargins(3, 3, 1, 3)
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setVerticalSpacing(1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.demoPlayPathLineEdit = bdlLineEdit(self.demoGroup)
        self.demoPlayPathLineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.demoPlayPathLineEdit.setPlaceholderText("Path to demo")
        self.demoPlayPathLineEdit.setObjectName("demoPlayPathLineEdit")
        self.gridLayout_9.addWidget(self.demoPlayPathLineEdit, 1, 3, 1, 1)
        self.demoPlayBrowseButton = QtWidgets.QPushButton(self.demoGroup)
        self.demoPlayBrowseButton.setMaximumSize(QtCore.QSize(20, 18))
        self.demoPlayBrowseButton.setText("...")
        self.demoPlayBrowseButton.setObjectName("demoPlayBrowseButton")
        self.gridLayout_9.addWidget(self.demoPlayBrowseButton, 1, 4, 1, 1)
        self.demoRecordNameLineEdit = QtWidgets.QLineEdit(self.demoGroup)
        self.demoRecordNameLineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.demoRecordNameLineEdit.setPlaceholderText("Name of demo")
        self.demoRecordNameLineEdit.setObjectName("demoRecordNameLineEdit")
        self.gridLayout_9.addWidget(self.demoRecordNameLineEdit, 0, 3, 1, 1)
        self.demoPlayRadio = QtWidgets.QRadioButton(self.demoGroup)
        self.demoPlayRadio.setText("Play")
        self.demoPlayRadio.setObjectName("demoPlayRadio")
        self.gridLayout_9.addWidget(self.demoPlayRadio, 1, 0, 1, 1)
        self.demoRecordBrowseButton = QtWidgets.QPushButton(self.demoGroup)
        self.demoRecordBrowseButton.setMaximumSize(QtCore.QSize(20, 18))
        self.demoRecordBrowseButton.setStyleSheet("QPushButton {\n"
"padding-left: 0px; padding-right: 0px;\n"
"}")
        self.demoRecordBrowseButton.setText("...")
        self.demoRecordBrowseButton.setObjectName("demoRecordBrowseButton")
        self.gridLayout_9.addWidget(self.demoRecordBrowseButton, 0, 4, 1, 1)
        self.demoRecordRadio = QtWidgets.QRadioButton(self.demoGroup)
        self.demoRecordRadio.setText("Record")
        self.demoRecordRadio.setChecked(True)
        self.demoRecordRadio.setObjectName("demoRecordRadio")
        self.gridLayout_9.addWidget(self.demoRecordRadio, 0, 0, 1, 1)
        self.demoAutoRecordCheck = QtWidgets.QCheckBox(self.demoGroup)
        self.demoAutoRecordCheck.setMaximumSize(QtCore.QSize(16777215, 21))
        self.demoAutoRecordCheck.setToolTip("<html><head/><body><p>Automatically start recording a new demo after the previous recording finishes. Mainly intended for speedrunners, who must restart frequently.</p><p>Appends an attempt number to the end of each file. Demos must be deleted manually.</p><p><span style=\" font-weight:600;\">This setting must be disabled while in-game.</span></p></body></html>")
        self.demoAutoRecordCheck.setText("Auto-record new demos")
        self.demoAutoRecordCheck.setObjectName("demoAutoRecordCheck")
        self.gridLayout_9.addWidget(self.demoAutoRecordCheck, 2, 0, 1, 5)
        self.gridLayout_8.addWidget(self.demoGroup, 0, 0, 1, 1)
        self.paramGroup = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.paramGroup.setMaximumSize(QtCore.QSize(16777215, 13))
        self.paramGroup.setToolTip("Change additional optional parameters\n"
"to alter your game.")
        self.paramGroup.setTitle("Show more parameters")
        self.paramGroup.setCheckable(True)
        self.paramGroup.setChecked(False)
        self.paramGroup.setObjectName("paramGroup")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.paramGroup)
        self.gridLayout_5.setContentsMargins(-1, 3, -1, 3)
        self.gridLayout_5.setVerticalSpacing(2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.paramFast = QtWidgets.QCheckBox(self.paramGroup)
        self.paramFast.setToolTip("Fast monsters, with dramatically\n"
"increased aggression and projectile\n"
"speeds. This setting is on by default\n"
"on NIGHTMARE! difficulty.\n"
"\n"
"Can be used outside of NIGHTMARE! to\n"
"spice up the other difficulty settings.")
        self.paramFast.setText("-fast")
        self.paramFast.setObjectName("paramFast")
        self.gridLayout_5.addWidget(self.paramFast, 0, 0, 1, 1)
        self.paramRespawn = QtWidgets.QCheckBox(self.paramGroup)
        self.paramRespawn.setToolTip("Demons will respawn after a short delay\n"
"once killed. This setting is on by default\n"
"on NIGHTMARE! difficulty.\n"
"\n"
"Can be used outside of NIGHTMARE! to\n"
"spice up the other difficulty settings.")
        self.paramRespawn.setText("-respawn")
        self.paramRespawn.setObjectName("paramRespawn")
        self.gridLayout_5.addWidget(self.paramRespawn, 0, 1, 1, 1)
        self.paramSoloNet = QtWidgets.QCheckBox(self.paramGroup)
        self.paramSoloNet.setToolTip("<html><head/><body><p style=\"line-height:0.125\">Starts a fake multiplayer game with</p><p style=\"line-height:0.125\">just you. Allows players to play</p><p style=\"line-height:0.125\">multiplayer-only versions of levels</p><p style=\"line-height:0.125\">in a singleplayer environment.</p><p style=\"line-height:0.125\"><br/></p><p style=\"line-height:0.125\">Using solo-net will also turn on</p><p style=\"line-height:0.125\">multiplayer rules, such as players</p><p style=\"line-height:0.125\">respawning when they die.</p><p style=\"line-height:0.125\"><br/></p><p><span style=\" font-weight:600;\">Not available in GZDoom.</span></p></body></html>")
        self.paramSoloNet.setText("-solo-net")
        self.paramSoloNet.setObjectName("paramSoloNet")
        self.gridLayout_5.addWidget(self.paramSoloNet, 1, 0, 1, 1)
        self.paramNoMonsters = QtWidgets.QCheckBox(self.paramGroup)
        self.paramNoMonsters.setToolTip("Removes demons from the game.\n"
"\n"
"This will break levels that require\n"
"killing specific monsters to exit.")
        self.paramNoMonsters.setText("-nomonsters")
        self.paramNoMonsters.setObjectName("paramNoMonsters")
        self.gridLayout_5.addWidget(self.paramNoMonsters, 1, 1, 1, 1)
        self.paramNoMusic = QtWidgets.QCheckBox(self.paramGroup)
        self.paramNoMusic.setToolTip("Disables music.")
        self.paramNoMusic.setText("-nomusic")
        self.paramNoMusic.setObjectName("paramNoMusic")
        self.gridLayout_5.addWidget(self.paramNoMusic, 2, 0, 1, 1)
        self.paramNoSFX = QtWidgets.QCheckBox(self.paramGroup)
        self.paramNoSFX.setToolTip("Disables sound effects.")
        self.paramNoSFX.setText("-nosfx")
        self.paramNoSFX.setObjectName("paramNoSFX")
        self.gridLayout_5.addWidget(self.paramNoSFX, 2, 1, 1, 1)
        self.paramNoSound = QtWidgets.QCheckBox(self.paramGroup)
        self.paramNoSound.setToolTip("Disables both music\n"
"and sound effects.")
        self.paramNoSound.setText("-nosound")
        self.paramNoSound.setObjectName("paramNoSound")
        self.gridLayout_5.addWidget(self.paramNoSound, 3, 0, 1, 1)
        self.gridLayout_8.addWidget(self.paramGroup, 2, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem7, 3, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabSettings, "Settings")
        self.tabTools = QtWidgets.QWidget()
        self.tabTools.setObjectName("tabTools")
        self.tabWidget.addTab(self.tabTools, "Tools")
        self.tabBDL = QtWidgets.QWidget()
        self.tabBDL.setObjectName("tabBDL")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabBDL)
        self.gridLayout_6.setContentsMargins(3, 12, 3, 12)
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
        self.bdlForceCapsCombo = QtWidgets.QComboBox(self.tabBDL)
        self.bdlForceCapsCombo.setMaximumSize(QtCore.QSize(55, 17))
        self.bdlForceCapsCombo.setCurrentText("Doom")
        self.bdlForceCapsCombo.setObjectName("bdlForceCapsCombo")
        self.bdlForceCapsCombo.addItem("")
        self.bdlForceCapsCombo.setItemText(0, "Doom")
        self.bdlForceCapsCombo.addItem("")
        self.bdlForceCapsCombo.setItemText(1, "DOOM")
        self.bdlForceCapsCombo.addItem("")
        self.bdlForceCapsCombo.setItemText(2, "DooM")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bdlForceCapsCombo)
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
        self.bdlRejectBadIWADs = QtWidgets.QCheckBox(self.tabBDL)
        self.bdlRejectBadIWADs.setToolTip("Displays a warning when an\n"
"invalid IWAD is detected.")
        self.bdlRejectBadIWADs.setText("Reject bad IWADs")
        self.bdlRejectBadIWADs.setChecked(True)
        self.bdlRejectBadIWADs.setObjectName("bdlRejectBadIWADs")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.bdlRejectBadIWADs)
        self.gridLayout_6.addLayout(self.formLayout, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tabBDL, "bdl")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        BDLMainWindow.setCentralWidget(self.centralwidget)
        self.portMenu = QtWidgets.QMenu()
        self.portMenu.setTitle("Source Ports")
        self.portMenu.setObjectName("portMenu")
        self.iwadMenu = QtWidgets.QMenu()
        self.iwadMenu.setTitle("IWADs")
        self.iwadMenu.setObjectName("iwadMenu")
        self.iwadMenuSteam = QtWidgets.QMenu(self.iwadMenu)
        self.iwadMenuSteam.setTitle("Purchase on Steam...")
        self.iwadMenuSteam.setObjectName("iwadMenuSteam")
        self.iwadMenuDeals = QtWidgets.QMenu(self.iwadMenu)
        self.iwadMenuDeals.setTitle("Check for deals...")
        self.iwadMenuDeals.setObjectName("iwadMenuDeals")
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
        self.portBrowseLocalFiles.setText("Open source port location...")
        self.portBrowseLocalFiles.setObjectName("portBrowseLocalFiles")
        self.iwadBrowseLocalFiles = QtWidgets.QAction(BDLMainWindow)
        self.iwadBrowseLocalFiles.setText("Open IWAD location...")
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
        self.portMenu.addAction(self.portBrowseLocalFiles)
        self.portMenu.addAction(self.portRename)
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

        self.tabWidget.setCurrentIndex(0)
        self.warpSkillCombo.setCurrentIndex(3)
        self.demoGroup.toggled['bool'].connect(self.warpGroup.setChecked)
        self.bdlAutoDetectIWADs.toggled['bool'].connect(self.bdlRejectBadIWADs.setEnabled)
        self.bdlAutoDetectIWADs.toggled['bool'].connect(self.bdlRejectBadIWADs.setChecked)
        QtCore.QMetaObject.connectSlotsByName(BDLMainWindow)







###############################################################################
        self.loadConfig()

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
        self.iwadList.itemDoubleClicked.connect(self.resetIWADFlags)
        self.iwadList.model().rowsInserted.connect(self.changeDoomCapitalization)
        self.iwadAdd.clicked.connect(lambda: self.prepareAddFile(self.iwadList))
        self.iwadRem.clicked.connect(lambda: self.removeListItem(self.iwadList))
        # TODO: crossplatform -> explorer /select is windows only
        self.iwadBrowseLocalFiles.triggered.connect(lambda: subprocess.Popen(f'explorer /select,{os.path.abspath(self.iwadList.currentItem().data(3))}'))
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
        # TODO: again, windows only ^^^
        self.portBrowseLocalFiles.triggered.connect(lambda: subprocess.Popen(f'explorer /select,{os.path.abspath(self.portCombo.currentData(3))}'))
        self.portRename.triggered.connect(self.renamePort)
        self.portRenameLineEdit.returnPressed.connect(self.renamePort)
        self.portMoveUp.triggered.connect(lambda: self.movePort('up'))
        self.portMoveDown.triggered.connect(lambda: self.movePort('down'))
        self.portMoveToTop.triggered.connect(lambda: self.movePort('top'))
        self.portMoveToBottom.triggered.connect(lambda: self.movePort('bottom'))

        self.demoRecordBrowseButton.clicked.connect(lambda: self.prepareAddFile(self.demoRecordNameLineEdit))
        self.demoPlayBrowseButton.clicked.connect(lambda: self.prepareAddFile(self.demoPlayPathLineEdit))

        self.demoGroup.toggled.connect(lambda: self.demoGroup.setMaximumHeight(80 if self.demoGroup.isChecked() else 13))
        self.warpGroup.toggled.connect(lambda: self.warpGroup.setMaximumHeight(69 if self.warpGroup.isChecked() else 13))
        self.paramGroup.toggled.connect(lambda: self.paramGroup.setMaximumHeight(16777215 if self.paramGroup.isChecked() else 13))

        self.bdlForceCaps.toggled.connect(self.changeDoomCapitalization)
        self.bdlForceCapsCombo.currentIndexChanged.connect(self.changeDoomCapitalization)
        self.bdlAutoDetectIWADs.toggled.connect(lambda: run.updateBDLSettings(self.bdlAutoDetectIWADs.isChecked(), self.bdlRejectBadIWADs.isChecked()))
        self.bdlRejectBadIWADs.toggled.connect(lambda: run.updateBDLSettings(self.bdlAutoDetectIWADs.isChecked(), self.bdlRejectBadIWADs.isChecked()))

        self.commandLinePreviewButton.clicked.connect(lambda: run.showPopup(title="Command line preview",
                                                                            text=self.prepareLaunch(noLaunch=True),
                                                                            icon=QtWidgets.QMessageBox.Information))

        # Extra stuff
        self.demoRecordNameLineEdit.setTextMargins(0,0,8,0)
        self.portRenameLineEdit.hide()
        self.lastDir = '.'          # Not tied to an existing widget
        self.autoRecording = False     # Not in config
        self.autoRecordTimer = QtCore.QTimer()
        self.autoRecordTimer.timeout.connect(self.autoRecordTimeout)
        self.autoRecordProcess = None
        self.autoRecordDemoAttempt = 1



    def firstTimeSetup(self):
        # TODO: also check updates
        #if os.path.exists("%APPDATA%\\Vectec Software\\qZDL.ini"):
        #    pass        # TODO: s t e a l ZDL's config
        #else:
        run.findSteamIWADs(self.iwadList)



    def loadConfig(self):
        if not os.path.exists("bdl.ini"):
            self.firstTimeSetup()
        else:
            config = configparser.ConfigParser()
            config.read("bdl.ini")

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

            # set window size/pos, splitter sizes, other settings
            if 'bdl.general' in config:
                windowSizeX, windowSizeY = config['bdl.general'].get('windowsize',fallback='225,247').split(",")
                BDLMainWindow.resize(int(windowSizeX), int(windowSizeY))
                windowPosX, windowPosY = config['bdl.general'].get('windowpos',fallback='350,250').split(",")
                BDLMainWindow.move(int(windowPosX), int(windowPosY))

                # each setting is wrapped in a try-except block to restore it to the default
                # set in Qt designer when the UI was created in case of user tampering
                general = config['bdl.general']
                try: self.splitter.setSizes(list(int(size) for size in general.get('lastsplittersize').split(',')))
                except: pass
                try: self.lastDir = general.get('lastdir', fallback='.')
                except: pass
                try: self.bdlAutoClose.setChecked(general.getboolean('autoclose', fallback=False))
                except: pass
                try: self.bdlForceCaps.setChecked(general.getboolean('forcecaps', fallback=True))
                except: pass
                try: self.bdlForceCapsCombo.setCurrentIndex(general.getint('forcecapsindex', fallback=0))
                except: pass
                try: self.bdlAutoDetectIWADs.setChecked(general.getboolean('autodetectiwads', fallback=True))
                except: pass
                try: self.bdlRejectBadIWADs.setChecked(general.getboolean('rejectbadiwads', fallback=True))
                except: pass

            if 'bdl.save' in config:
                save = config['bdl.save']
                try: self.parameterLineEdit.setText(save.get('extra', fallback=''))
                except: pass
                try: self.portCombo.setCurrentIndex(save.getint('portindex', fallback=0))
                except: pass
                try: self.iwadList.setCurrentRow(save.getint('iwadindex', fallback=0))
                except: pass
                try: self.complevelCombo.setCurrentIndex(save.getint('complevelindex', fallback=0))
                except: pass

                try: self.demoGroup.setChecked(save.getboolean('demoenabled', fallback=False))
                except: pass
                try: self.demoRecordRadio.setChecked(save.getboolean('demorecord', fallback=False))
                except: pass
                try: self.demoRecordNameLineEdit.setText(save.get('demorecordname', fallback=''))
                except: pass
                try: self.demoPlayRadio.setChecked(save.getboolean('demoplay', fallback=False))
                except: pass
                try: self.demoPlayPathLineEdit.setText(save.get('demoplaypath', fallback=''))
                except: pass
                try: self.demoAutoRecordCheck.setChecked(save.getboolean('demoautorecord', fallback=False))
                except: pass

                try: self.warpGroup.setChecked(save.getboolean('warpenabled', fallback=False))
                except: pass
                #try: self.warpMapCombo.setCurrentIndex(save.getint('warp', fallback=0))
                #except: pass
                try: self.warpSkillCombo.setCurrentIndex((save.getint('skill', fallback=4))-1)
                except: pass    # skill config is 1-5 instead of index (0-4) to match up with how doom reads the -skill parameter

            if 'bdl.moreparameters' in config:
                params = config['bdl.moreparameters']
                try: self.paramGroup.setChecked(params.getboolean('showmoreparameters', fallback=False))
                except: pass
                try: self.paramFast.setChecked(params.getboolean('fast', fallback=False))
                except: pass
                try: self.paramRespawn.setChecked(params.getboolean('respawn', fallback=False))
                except: pass
                try: self.paramSoloNet.setChecked(params.getboolean('solo-net', fallback=False))
                except: pass
                try: self.paramNoMonsters.setChecked(params.getboolean('nomonsters', fallback=False))
                except: pass
                try: self.paramNoMusic.setChecked(params.getboolean('nomusic', fallback=False))
                except: pass
                try: self.paramNoSFX.setChecked(params.getboolean('nosfx', fallback=False))
                except: pass
                try: self.paramNoSound.setChecked(params.getboolean('nosound', fallback=False))
                except: pass

            self.demoGroup.setMaximumHeight(80 if self.demoGroup.isChecked() else 13)
            self.warpGroup.setMaximumHeight(69 if self.warpGroup.isChecked() else 13)
            self.paramGroup.setMaximumHeight(16777215 if self.paramGroup.isChecked() else 13)
            run.updateBDLSettings(self.bdlAutoDetectIWADs, self.bdlRejectBadIWADs)



    def saveConfig(self):       # TODO: add md5 check here? might not save time
        config = configparser.ConfigParser()
        config['bdl.general'] = {}
        general = config['bdl.general']
        general['lastdir'] = self.lastDir
        general['autoclose'] = str(self.bdlAutoClose.isChecked())
        general['forcecaps'] = str(self.bdlForceCaps.isChecked())
        general['forcecapsindex'] = str(self.bdlForceCapsCombo.currentIndex())
        general['autodetectiwads'] = str(self.bdlAutoDetectIWADs.isChecked())
        general['rejectbadiwads'] = str(self.bdlRejectBadIWADs.isChecked())

        general['windowpos'] = str(BDLMainWindow.x()-1) + ',' + str(BDLMainWindow.y()-31)   # -1 and -31 due to unknown offset
        general['windowsize'] = str(self.centralwidget.frameGeometry().width()) + ',' + str(self.centralwidget.frameGeometry().height())
        general['lastsplittersize'] = ','.join(str(size) for size in self.splitter.sizes())

        config['bdl.save'] = {}
        save = config['bdl.save']
        save['extra'] = self.parameterLineEdit.text()
        save['portindex'] = str(self.portCombo.currentIndex())
        save['iwadindex'] = str(self.iwadList.currentRow())
        save['complevelindex'] = str(self.complevelCombo.currentIndex())
        save['demoenabled'] = str(self.demoGroup.isChecked())
        save['demorecord'] = str(self.demoRecordRadio.isChecked())
        save['demorecordname'] = self.demoRecordNameLineEdit.text()
        save['demoplay'] = str(self.demoPlayRadio.isChecked())
        save['demoplaypath'] = self.demoPlayPathLineEdit.text()
        save['demoautorecord'] = str(self.demoAutoRecordCheck.isChecked())
        save['warpenabled'] = str(self.warpGroup.isChecked())
        save['warp'] = str(self.warpMapCombo.currentIndex())
        save['skill'] = str(self.warpSkillCombo.currentIndex()+1)   # +1 to negate the -1 in loadConfig()

        config['bdl.moreparameters'] = {}
        params = config['bdl.moreparameters']
        params['showmoreparameters'] = str(self.paramGroup.isChecked())
        params['fast'] = str(self.paramFast.isChecked())
        params['respawn'] = str(self.paramRespawn.isChecked())
        params['solo-net'] = str(self.paramSoloNet.isChecked())
        params['nomonsters'] = str(self.paramNoMonsters.isChecked())
        params['nomusic'] = str(self.paramNoMusic.isChecked())
        params['nosfx'] = str(self.paramNoSFX.isChecked())
        params['nosound'] = str(self.paramNoSound.isChecked())

        # loop through file widgets and save all wads/ports and their properties
        config['bdl.iwads'] = {}
        config['bdl.pwads'] = {}
        config['bdl.ports'] = {}
        for i, iwad in enumerate(self.getListWidgetItems(self.iwadList)):
            config['bdl.iwads'][f'iwadname{i}'] = iwad.text()
            config['bdl.iwads'][f'iwadpath{i}'] = iwad.data(3)
        for i, pwad in enumerate(self.getListWidgetItems(self.pwadList)):
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
        activeSettings = ""
        for i in range(self.pwadList.count()):
            pwad = self.pwadList.item(i)
            if pwad.checkState() == 2:      # 2 -> item is checked, isChecked() not available
                filePath = pwad.data(3)
                if filePath.endswith('.deh') or filePath.endswith('.bex'):
                    activeDEH += os.path.abspath(filePath) + " "
                else:
                    activePWADs += os.path.abspath(filePath) + " "

        if self.demoGroup.isChecked():
            if self.demoRecordRadio.isChecked():
                #if self.demoAutoRecordCheck.isChecked() and not isinstance(demoAttempt, int):
                #    self.autoRecordDemoAttempt     # if auto-record is checked and demoAttempt is "", start at 1
                demoDestination = self.demoRecordNameLineEdit.text().replace('.lmp', '').split(os.sep)
                demoPath = (os.sep).join(demoDestination[:-1])
                demoName = demoDestination[-1]
                for invalidChar in "\\/:*?<>| ":
                    demoName = demoName.replace(invalidChar, "")
                if not demoName:
                    demoName = "unnamed_demo"
                demoDestination = demoPath + os.sep + demoName
                activeSettings += f" -record {demoDestination + str(self.autoRecordDemoAttempt if self.demoAutoRecordCheck.isChecked() else '')}"
            elif self.demoPlayRadio.isChecked():
                activeSettings += f" -playdemo {self.demoPlayPathLineEdit.text()}"

        if self.warpGroup.isChecked():
            # TODO add something for the map here
            activeSettings += f" -skill {self.warpSkillCombo.currentIndex()+1}"

        # parameters typed out instead of using .text() for simplicity,
        # and in case I change the text of the checkboxes in the future.
        if self.paramGroup.isChecked():
            if self.paramFast.isChecked():       activeSettings += " -fast"
            if self.paramRespawn.isChecked():    activeSettings += " -respawn"
            if self.paramSoloNet.isChecked():    activeSettings += " -solo-net"
            if self.paramNoMonsters.isChecked(): activeSettings += " -nomonsters"
            if self.paramNoMusic.isChecked():    activeSettings += " -nomusic"
            if self.paramNoSFX.isChecked():      activeSettings += " -nosfx"
            if self.paramNoSound.isChecked():    activeSettings += " -nosound"

        try:
            process = run.run(port=self.portCombo.currentData(3),
                              iwad=self.iwadList.currentItem().data(3),
                              complevel=self.complevelCombo.currentData(3) if not self.demoPlayRadio.isChecked() else None,
                              pwads=activePWADs,        # ^^^ if demo is going to play, ignore the complevel dropdown
                              deh=activeDEH,
                              settings=activeSettings,
                              extra=self.parameterLineEdit.text(),
                              noLaunch=noLaunch)
            if self.demoAutoRecordCheck.isChecked() and not self.autoRecordTimer.isActive():
                self.autoRecordProcess = process
                self.autoRecordTimer.start(500)
            if noLaunch: return process     # process is actually the commandline when noLaunch is on
            elif self.bdlAutoClose.isChecked(): BDLMainWindow.close()   # only close if auto-record and noLaunch are off

        # TODO: add custom doom warning icons, move warning explanation elsewhere?
        # TODO: add logger?
        except AttributeError:      # AttributeError means no IWAD -> NoneType.data(3) causes it
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
        except TypeError:       # TypeError means no port -> '"' + NoneType + '"' in run.run() causes it
            run.showPopup(title="Missing source port!",
                                text="No source port detected! Both a source port and\n"
                                "a valid IWAD are required to run Doom games.",
                                textInformative=("Source ports are ports of Doom's original source\n"
                                                 "code, and are used to run game data.\n"
                                                 "Examples: PrBoom+, GZDoom, Chocolate Doom\n\n"
                                                 "IWADs are official game data files. They contain all of the\n"
                                                 "game's assets, and are used as the base for custom wads.\n"
                                                 "Examples: DOOM.WAD, DOOM2.WAD, TNT.WAD, etc."))

    def prepareAddFile(self, widget, files=None):
        self.lastDir = run.addFile(widget=widget,
                                   files=files,
                                   lastDir=self.lastDir)

    def autoRecordTimeout(self):
        if self.demoAutoRecordCheck.isChecked() and isinstance(self.autoRecordProcess, subprocess.Popen) and self.autoRecordProcess.poll() is not None:
            self.autoRecordTimer.stop()
            self.autoRecordDemoAttempt += 1
            self.prepareLaunch()

    def changeDoomCapitalization(self):
        if self.bdlForceCaps.isChecked():
            capsStyle = self.bdlForceCapsCombo.currentText()
            for iwad in self.getListWidgetItems(self.iwadList):
                try:
                    oldName = iwad.text()
                    nameIndex = oldName.lower().find("doom")
                    if nameIndex != -1:
                        iwad.setText(oldName[:nameIndex] + capsStyle + oldName[nameIndex+4:])
                except: continue

    def renamePort(self):
        if not self.portRenameLineEdit.isVisible():     # rename started
            self.portRenameLineEdit.show()      # show lineEdit to rename
            self.portRenameLineEdit.setText(self.portCombo.currentText())   # start with original name
            self.portRenameLineEdit.selectAll()     # start with text selected
            self.portRenameLineEdit.setFocus(QtCore.Qt.NoFocusReason)   # grab focus to type immediately


        else:   # rename finished
            newName = self.portRenameLineEdit.text()
            if newName:  # if the lineEdit is blank, don't change the name
                self.portCombo.setItemText(self.portCombo.currentIndex(), newName)   # change name
            self.portRenameLineEdit.hide()  # hide lineEdit

    def movePort(self, direction):
        try:
            portText = self.portCombo.currentText()
            portData = self.portCombo.currentData(3)
            portIndex = self.portCombo.currentIndex()
            newIndex = 0

            if direction == "up":       newIndex = portIndex - 1
            elif direction == "down":   newIndex = portIndex + 1
            elif direction == "top":    newIndex = 0
            elif direction == "bottom": newIndex = self.portCombo.count() - 1

            self.portCombo.removeItem(portIndex)
            self.portCombo.insertItem(newIndex, portText)
            self.portCombo.setItemData(newIndex, portData, 3)
            self.portCombo.setCurrentIndex(newIndex)
        except: pass

    def getListWidgetItems(self, listWidget):
        for i in range(listWidget.count()):
            yield listWidget.item(i)

    def removeListItem(self, qlist):
        selected = list(qlist.row(item) for item in qlist.selectedItems())  # generates list of currently selected item indexes
        selected.sort(reverse=True)                  # sorts list to delete higher indexes first to avoid indexes being updated
        for index in selected:         # uses takeItem() to remove items and deletes them manually since qt won't do it for you
            garbage = qlist.takeItem(index)
            del garbage

    def resetIWADFlags(self):   # Workaround for Qt bug in which dragging resets list item flags.
        try:
            self.iwadList.currentItem().setFlags(QtCore.Qt.ItemIsSelectable|
                                                 QtCore.Qt.ItemIsEditable|
                                                 QtCore.Qt.ItemIsDragEnabled|
                                                 QtCore.Qt.ItemIsEnabled)
        except: pass        # Try-except block to prevent crash with no iwads



    def openAboutDialog(self):
        aboutDialog = QtWidgets.QDialog()
        aboutDialog.setWindowModality(1)
        ui = window_about.Ui_aboutDialog()
        ui.setupUi(aboutDialog)
        aboutDialog.exec()



from bdlComboBox import bdlComboBox
from bdlListWidget import bdlListWidget
from bdlLineEdit import bdlLineEdit
import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BDLMainWindow = QtWidgets.QMainWindow()
    ui = Ui_BDLMainWindow()
    ui.setupUi(BDLMainWindow)
    BDLMainWindow.show()
    response = app.exec_()
    ui.saveConfig()
    sys.exit(response)