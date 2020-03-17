# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\res\window_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import window_about, run
import hashlib

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
        spacerItem1 = QtWidgets.QSpacerItem(5000, 10, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.pwadHLayout.addItem(spacerItem1)
        self.leftVLayout.addLayout(self.pwadHLayout)
        self.pwadList = bdlListWidget(self.layoutWidget, 'pwad')
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
        self.portLabel.setToolTip("<html><head/><body><p>Install new or add previously existing source ports here.</p><p>Source ports are ports of Doom\'s source code and are the basis through which all game data (WADs) are played.</p></body></html>")
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
        spacerItem3 = QtWidgets.QSpacerItem(5000, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.portHLayout.addItem(spacerItem3)
        self.rightVLayout.addLayout(self.portHLayout)
        self.portCombo = bdlComboBox(self.layoutWidget_2, 'port')
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
        spacerItem6 = QtWidgets.QSpacerItem(5000, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.iwadHLayout.addItem(spacerItem6)
        self.rightVLayout.addLayout(self.iwadHLayout)
        self.iwadList = bdlListWidget(self.layoutWidget_2, 'iwad')
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
"background-color: rgb(235, 235, 235);\n"
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
        self.complevelCombo.setToolTip("<html><head/><body><p>Complevels, or compatibilty levels, are used by PrBoom+ and GLBoom+ to emulate various Doom versions and formats. This dropdown features the most common complevels.</p><p>If you\'re playing a custom wad, look for &quot;complevel&quot;, &quot;cl&quot;, a source port, or a specific format (vanilla, limit-removing, boom, MBF, UDMF) mentioned in its description, to know what to pick. If it says &quot;vanilla&quot; or &quot;limit-removing&quot; and its for Doom 2, pick complevel 2. If it says &quot;UDMF&quot; or &quot;Hexen in Doom 2&quot;, pick a ZDoom source port.</p><p>This dropdown can be overridden by manually specifying a complevel as one of your extra command line arguments. </p><p><span style=\" font-weight:600;\">This dropdown has no effect on other source ports.</span></p></body></html>")
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
        self.formLayout_2 = QtWidgets.QFormLayout(self.tabSettings)
        self.formLayout_2.setObjectName("formLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tabSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 56))
        self.groupBox.setTitle("Warp to level")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 201, 20))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout_4)
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
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.aboutButton = QtWidgets.QPushButton(self.tabBDL)
        self.aboutButton.setMaximumSize(QtCore.QSize(46, 21))
        self.aboutButton.setText("About")
        self.aboutButton.setObjectName("aboutButton")
        self.gridLayout_6.addWidget(self.aboutButton, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabBDL, "bdl")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        BDLMainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(BDLMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 225, 21))
        self.menuBar.setObjectName("menuBar")
        self.portMenu = QtWidgets.QMenu(self.menuBar)
        self.portMenu.setTitle("Source Ports")
        self.portMenu.setObjectName("portMenu")
        BDLMainWindow.setMenuBar(self.menuBar)
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
        self.portMenu.addAction(self.portAdd)
        self.portMenu.addAction(self.portRem)
        self.portMenu.addSeparator()
        self.portMenu.addAction(self.portRename)
        self.portMenu.addSeparator()
        self.portMenu.addAction(self.portMoveUp)
        self.portMenu.addAction(self.portMoveDown)
        self.portMenu.addAction(self.portMoveToBottom)
        self.portMenu.addAction(self.portMoveToTop)
        self.portMenu.addSeparator()
        self.portMenu.addAction(self.portDownloadAction)
        self.menuBar.addAction(self.portMenu.menuAction())

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BDLMainWindow)








        self.complevelCombo.setItemData(0, "-complevel 2", 3)
        self.complevelCombo.setItemData(1, "-complevel 3", 3)
        self.complevelCombo.setItemData(2, "-complevel 4", 3)
        self.complevelCombo.setItemData(3, "-complevel 9", 3)
        self.complevelCombo.setItemData(4, "-complevel 11", 3)

        self.launchButton.clicked.connect(self.prepareLaunch)
        self.aboutButton.clicked.connect(self.openAboutDialog)

        self.pwadAdd.clicked.connect(lambda: run.addFile(self.pwadList))
        self.pwadRem.clicked.connect(lambda: self.removeListItem(self.pwadList))

        self.iwadList.itemDoubleClicked.connect(self.resetFlags)
        self.iwadAdd.clicked.connect(lambda: run.addFile(self.iwadList))
        self.iwadRem.clicked.connect(lambda: self.removeListItem(self.iwadList))

        self.portMenuButton.setMenu(self.portMenu)
        self.portAdd.triggered.connect(lambda: run.addFile(self.portCombo))
        self.portRem.triggered.connect(lambda: self.portCombo.removeItem(self.portCombo.currentIndex()))


    def resetFlags(self):       # Workaround for Qt bug in which dragged list items have their flags reset to default.
        try:                    # Try-except block to prevent crash when launching with no iwads
            self.iwadList.currentItem().setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        except:
            pass

    def removeListItem(self, qlist):
        selected = list(qlist.row(item) for item in qlist.selectedItems())      # generates list of currently selected item indexes
        selected.sort(reverse=True)                     # sorts list to delete higher indexes first to avoid indexes being updated
        for index in selected:          # uses takeItem() to remove items and deletes them manually since qt won't do it for you
            garbage = qlist.takeItem(index)
            del garbage

    def prepareLaunch(self):
        activePWADs = ""
        activeDEH = ""
        for i in range(self.pwadList.count()):
            pwad = self.pwadList.item(i)
            if pwad.checkState() == 2:                  # 2 -> item is checked
                filePath = pwad.data(3)
                if filePath.endswith("deh") or filePath.endswith("bex"):
                    activeDEH += filePath + " "
                else:
                    activePWADs += filePath + " "

        run.run(port=self.portCombo.currentData(3),
                iwad=self.iwadList.currentItem().data(3),
                complevel=self.complevelCombo.currentData(3),
                pwads=activePWADs,
                deh=activeDEH,
                warp=0,
                skill=0,
                extra=self.parameterLineEdit.text())

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
