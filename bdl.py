from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os, subprocess, hashlib, webbrowser
from datetime import datetime
import window_main, window_about, bdlWidgets, config, update
from names import portNames, iwadNames, iwadNamesSimple, mapNumberStyles

# TODO: add full auto-sort for ports+iwads
# TODO: add fallback for empty wad/port names
# TODO: add logger

class MissingPortAndIWAD(Exception):
    pass
class MissingPort(Exception):
    pass
class MissingIWAD(Exception):
    pass



class BDLInstance:
    bdlVersion = 6
    bdlVersionStr = '0.0.6 alpha'

    def setupBDL(self, ui, window):
        self.ui = ui
        self.window = window
        self.ui.menuBar.hide()  # TODO: qt designer can't add menus with a menubar???
        bdlWidgets.setBDLInstance(self)

        self.lastDir = '.'
        self.updateReady = False
        self.bdlAutoDetectIWADs = True
        self.bdlRejectBadIWADs = True
        config.loadConfig(self)

        self.connectWidgetSignals()
        update.checkUpdateSuccess(self)

        if self.updateReady:    # update is still queued from previous session
            self.ui.tabWidget.setTabText(3, 'bdl (!)')
            self.ui.bdlUpdateButton.setToolTip('An update was found for you last session.')
            self.ui.bdlUpdateButton.setEnabled(True)
        else:   # no update queued -> if it's a new day check for updates
            try:
                if self.ui.bdlAutoUpdateCheck.isChecked():
                    lastCheck = datetime.strptime(self.ui.bdlUpdateLastCheckLabel.text(),'Last check: %m/%d/%y').date()
                    today = datetime.now().date()
                    if today > lastCheck:
                        update.checkUpdate(self)
            except: pass

        # Extra stuff
        self.ui.complevelCombo.setItemData(0, "-complevel 2", 3)
        self.ui.complevelCombo.setItemData(1, "-complevel 3", 3)
        self.ui.complevelCombo.setItemData(2, "-complevel 4", 3)
        self.ui.complevelCombo.setItemData(3, "-complevel 9", 3)
        self.ui.complevelCombo.setItemData(4, "-complevel 11", 3)

        self.autoRecording = False     # Not in config
        self.autoRecordTimer = QtCore.QTimer()
        self.autoRecordTimer.timeout.connect(self.autoRecordTimeout)
        self.autoRecordProcess = None
        self.autoRecordDemoAttempt = 1
        self.autoRecordDemoSession = 1

        self.ui.portRenameLineEdit.hide()
        self.ui.demoGroup.setMaximumHeight(80 if self.ui.demoGroup.isChecked() else 13)
        self.ui.warpGroup.setMaximumHeight(69 if self.ui.warpGroup.isChecked() else 13)
        self.ui.paramGroup.setMaximumHeight(16777215 if self.ui.paramGroup.isChecked() else 13)
        self.ui.demoRecordNameLineEdit.setTextMargins(0,0,8,0)
        self.ui.bdlDownloadLabel.hide()
        self.ui.bdlDownloadProgress.hide()
        self.resetPWADsCheckable()



    def connectWidgetSignals(self):
        # Connecting slots, signals, and menus
        self.ui.iwadMenuButton.setMenu(self.ui.iwadMenu)
        self.ui.portMenuButton.setMenu(self.ui.portMenu)
        self.ui.bdlMenuButton.setMenu(self.ui.bdlMenu)

        self.ui.launchButton.clicked.connect(self.prepareLaunch)

        self.ui.pwadAdd.clicked.connect(lambda: self.addFile(self.ui.pwadList))
        self.ui.pwadRem.clicked.connect(lambda: self.removeListItem(self.ui.pwadList))

        self.ui.iwadList.itemDoubleClicked.connect(self.resetIWADFlags)
        self.ui.iwadList.model().rowsInserted.connect(self.changeDoomCapitalization)
        self.ui.iwadList.currentItemChanged[QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem].connect(self.fillWarpMapCombo)
        self.ui.iwadAdd.clicked.connect(lambda: self.addFile(self.ui.iwadList))
        self.ui.iwadRem.clicked.connect(lambda: self.removeListItem(self.ui.iwadList))
        # TODO: crossplatform -> explorer /select is windows only

        self.ui.iwadBrowseLocalFiles.triggered.connect(lambda: subprocess.Popen(f'explorer /select,{os.path.abspath(self.ui.iwadList.currentItem().data(3))}'))
        self.ui.iwadClearAll.triggered.connect(lambda: self.clearListWidgetItems(self.ui.iwadList))
        self.ui.iwadAutoAddSteamIWADs.triggered.connect(lambda: config.findSteamIWADs(self))
        self.ui.iwadSteamUDoom.triggered.connect(lambda: webbrowser.open('https://store.steampowered.com/app/2280/Ultimate_Doom/'))
        self.ui.iwadSteamDoom2.triggered.connect(lambda: webbrowser.open('https://store.steampowered.com/app/2300/DOOM_II/'))
        self.ui.iwadSteamFinalDoom.triggered.connect(lambda: webbrowser.open('https://store.steampowered.com/app/2290/Final_DOOM/'))
        self.ui.iwadSteamClassicComplete.triggered.connect(lambda: webbrowser.open('https://store.steampowered.com/sub/18397/'))
        self.ui.iwadDealsUDoom.triggered.connect(lambda: webbrowser.open('https://isthereanydeal.com/game/ultimatedoom/info/'))
        self.ui.iwadDealsDoom2.triggered.connect(lambda: webbrowser.open('https://isthereanydeal.com/game/doomii/info/'))
        self.ui.iwadDealsFinalDoom.triggered.connect(lambda: webbrowser.open('https://isthereanydeal.com/game/finaldoom/info/'))
        self.ui.iwadDealsClassicComplete.triggered.connect(lambda: webbrowser.open('https://isthereanydeal.com/game/doomclassiccomplete/info/'))

        self.ui.portAdd.triggered.connect(lambda: self.addFile(self.ui.portCombo))
        self.ui.portRem.triggered.connect(lambda: self.ui.portCombo.removeItem(self.ui.portCombo.currentIndex()))
        self.ui.portClearAll.triggered.connect(lambda: self.clearPorts())
        # TODO: again, windows only
        self.ui.portBrowseLocalFiles.triggered.connect(lambda: subprocess.Popen(f'explorer /select,{os.path.abspath(self.ui.portCombo.currentData(3))}'))
        self.ui.portRename.triggered.connect(self.renamePort)
        self.ui.portRenameLineEdit.returnPressed.connect(self.renamePort)
        self.ui.portMoveUp.triggered.connect(lambda: self.movePort('up'))
        self.ui.portMoveDown.triggered.connect(lambda: self.movePort('down'))
        self.ui.portMoveToTop.triggered.connect(lambda: self.movePort('top'))
        self.ui.portMoveToBottom.triggered.connect(lambda: self.movePort('bottom'))

        self.ui.demoGroup.toggled.connect(lambda: self.ui.demoGroup.setMaximumHeight(80 if self.ui.demoGroup.isChecked() else 13))
        self.ui.warpGroup.toggled.connect(lambda: self.ui.warpGroup.setMaximumHeight(69 if self.ui.warpGroup.isChecked() else 13))
        self.ui.paramGroup.toggled.connect(lambda: self.ui.paramGroup.setMaximumHeight(16777215 if self.ui.paramGroup.isChecked() else 13))

        self.ui.demoRecordBrowseButton.clicked.connect(lambda: self.addFile(self.ui.demoRecordNameLineEdit))
        self.ui.demoPlayBrowseButton.clicked.connect(lambda: self.addFile(self.ui.demoPlayPathLineEdit))
        self.ui.demoRecordNameLineEdit.textChanged.connect(lambda: self.ui.demoRecordRadio.setChecked(True))
        self.ui.demoRecordNameLineEdit.selectionChanged.connect(lambda: self.ui.demoRecordRadio.setChecked(True))
        self.ui.demoPlayPathLineEdit.textChanged.connect(lambda: self.ui.demoPlayRadio.setChecked(True))
        self.ui.demoPlayPathLineEdit.selectionChanged.connect(lambda: self.ui.demoPlayRadio.setChecked(True))

        self.ui.bdlCapitalization.toggled.connect(self.changeDoomCapitalization)
        self.ui.bdlCapitalizationCombo.currentIndexChanged.connect(self.changeDoomCapitalization)
        self.ui.bdlPWADsCheckable.toggled.connect(self.resetPWADsCheckable)
        self.ui.bdlUpdateCheckNowButton.clicked.connect(lambda: update.checkUpdate(self))
        self.ui.bdlUpdateButton.clicked.connect(lambda: update.update(self))

        self.ui.bdlMenuSaveini.triggered.connect(self.saveCustomConfig)
        self.ui.bdlMenuLoadini.triggered.connect(self.loadCustomConfig)
        self.ui.bdlMenuClearEverything.triggered.connect(self.clearEverything)
        self.ui.bdlMenuAbout.triggered.connect(self.openAboutDialog)

        self.ui.commandLinePreviewButton.clicked.connect(lambda: self.showPopup(title="Command line preview",
                                                                                text=self.prepareLaunch(noLaunch=True),
                                                                                icon=QtWidgets.QMessageBox.Information))



    def prepareLaunch(self, noLaunch=False):
      ### Error Handling ###
        errorText = ("Source ports are ports of Doom's original source\n"
                     "code, and are used to run game data.\n"
                     "Examples: PrBoom+, GZDoom, Chocolate Doom\n\n"
                     "IWADs are official game data files. They contain all of the\n"
                     "game's assets, and are used as the base for custom wads.\n"
                     "Examples: DOOM.WAD, DOOM2.WAD, TNT.WAD, etc.")
        try:
            if self.ui.portCombo.currentIndex() == -1 and self.ui.iwadList.currentItem() == None:
                raise MissingPortAndIWAD
            elif self.ui.portCombo.currentIndex() == -1:
                raise MissingPort
            elif self.ui.iwadList.currentItem() == None:
                raise MissingIWAD

        # TODO: add custom doom warning icons?
        except MissingPortAndIWAD:
            self.showPopup(title="Missing source port and IWAD!",
                           text="No source port or IWAD detected! Both a source port\n"
                           "and a valid IWAD are required to run Doom games.",
                           textInformative=errorText)
            return
        except MissingPort:       # TypeError means no port -> '"' + NoneType + '"' above causes it
            self.showPopup(title="Missing source port!",
                                text="No source port detected! Both a source port and\n"
                                "a valid IWAD are required to run Doom games.",
                                textInformative=errorText)
            return
        except MissingIWAD:      # AttributeError means no IWAD -> NoneType.data(3) causes it
            self.showPopup(title="Missing IWAD!",
                           text="No IWAD detected! Both a source port and a\n"
                           "valid IWAD are required to run Doom games.",
                           textInformative=errorText)
            return

      ### Launching ###
        port = self.ui.portCombo.currentData(3)
        iwad = self.ui.iwadList.currentItem().data(3)
        complevel = self.ui.complevelCombo.currentData(3) if not self.ui.demoPlayRadio.isChecked() else ""
        activePWADs = ""
        activeDEH = ""
        activeSettings = ""
        extra=self.ui.parameterLineEdit.text()

        for i in range(self.ui.pwadList.count()):
            pwad = self.ui.pwadList.item(i)
            # make sure checkboxes are enabled, 2 = checked (no isChecked() for some reason)
            if not self.ui.bdlPWADsCheckable.isChecked() or pwad.checkState() == 2:
                filePath = pwad.data(3)
                if filePath.endswith('.deh') or filePath.endswith('.bex'):
                    activeDEH += os.path.abspath(filePath) + " "
                else:
                    activePWADs += os.path.abspath(filePath) + " "

        if self.ui.demoGroup.isChecked():
            # TODO: clean this up
            if self.ui.demoRecordRadio.isChecked():
                demoDestination = self.ui.demoRecordNameLineEdit.text().replace('.lmp', '').split(os.sep)
                demoPath = (os.sep).join(demoDestination[:-1])

                demoName = demoDestination[-1]
                for invalidChar in "\\/:*?<>| ":
                    demoName = demoName.replace(invalidChar, "")
                if not demoName: demoName = "unnamed_demo"

                if demoPath:
                    self.lastDir = demoPath
                    demoDestination = demoPath + os.sep + demoName
                else:
                    self.lastDir = '.'
                    demoDestination = demoName

                if self.ui.demoAutoRecordCheck.isChecked():
                    demoTempDest = demoDestination
                    demoDestination += '_' + str(self.autoRecordDemoSession) + '_' + str(self.autoRecordDemoAttempt)

                    while os.path.exists(demoDestination + '.lmp'):
                        self.autoRecordDemoSession += 1
                        demoDestination = demoTempDest + '_' + str(self.autoRecordDemoSession) + '_' + str(self.autoRecordDemoAttempt)

                activeSettings += f" -record {demoDestination}"
                if self.ui.demoLongTicsCheck.isChecked():
                    activeSettings += " -longtics"
                if not self.ui.warpGroup.isChecked():
                    activeSettings += " -skill 4"
            elif self.ui.demoPlayRadio.isChecked():
                activeSettings += f" -playdemo {self.ui.demoPlayPathLineEdit.text()}"

        if self.ui.warpGroup.isChecked():
            if self.ui.warpGroup.isEnabled():
                warpMap = self.ui.warpMapCombo.currentText()
                if warpMap:
                    if warpMap.startswith('E'):
                        activeSettings += f" -warp {warpMap[1]} {warpMap[3]}"   # E3M4 -> 3 4
                    elif warpMap.startswith('MAP'):
                        activeSettings += f" -warp {warpMap[3:]}"   # MAP25 -> 25

                activeSettings += f" -skill {self.ui.warpSkillCombo.currentIndex()+1}"
            else:
                activeSettings += f" -skill 4"

        # TODO: loop + use data/.text() instead, or leave it like this for readability?
        if self.ui.paramGroup.isChecked():
            if self.ui.paramFast.isChecked():       activeSettings += " -fast"
            if self.ui.paramRespawn.isChecked():    activeSettings += " -respawn"
            if self.ui.paramSoloNet.isChecked():    activeSettings += " -solo-net"
            if self.ui.paramLevelStat.isChecked():  activeSettings += " -levelstat"
            if self.ui.paramNoSound.isChecked():    activeSettings += " -nosound"
            if self.ui.paramNoMonsters.isChecked(): activeSettings += " -nomonsters"
            if self.ui.paramNoMusic.isChecked():    activeSettings += " -nomusic"
            if self.ui.paramNoSFX.isChecked():      activeSettings += " -nosfx"
            if self.ui.paramTurboCheck.isChecked(): activeSettings += f" -turbo {self.ui.paramTurboSpin.value()}"

        try:
            command = '"' + os.path.abspath(port) + '"'
            command += f" -iwad {os.path.abspath(iwad)}"
            if activePWADs: command += f" -file {activePWADs}"
            if activeDEH: command += f" -deh {activeDEH}"
            command += f" {complevel}"
            command += f" {activeSettings}"
            command += f" {extra}"

            print(command)
            if noLaunch: return command
            command = subprocess.Popen(command)  # Popen prevents bdl from hanging while game is open

            if self.ui.demoAutoRecordCheck.isChecked() and not self.autoRecordTimer.isActive():
                self.autoRecordProcess = command
                self.autoRecordTimer.start(500)

            if self.ui.bdlAutoClose.isChecked() and not self.isRecordingDemo(): self.window.close()
            return command

        except Exception as error:
            print('Unexpected bdl.prepareLaunch() error:',error)



    # TODO: oh gosh none of this will work outside windows will it
    def addFile(self, widget, files=None, dragAndDropped=False):
        if not dragAndDropped: newLastDir = self.lastDir

        ##### PWADS #####
        if widget.objectName() == "pwadList":
            if files is None:
                files = QtWidgets.QFileDialog.getOpenFileNames(caption="Select one or more files to add",
                                                               directory=self.lastDir,
                                                               filter="DOOM files (*.wad *.zip *.deh *.bex *.pk3 *.pk7 *.pkz *.ipk7 *p7z);;"
                                                               "Vanilla Doom files (*.wad *.zip *.deh);;"
                                                               "Boom files (*.wad *.zip *.deh *.bex);;"
                                                               "ZDoom files (*.pk3 *.pk7 *.pkz *.ipk7 *p7z);;"
                                                               "Patch files (*.deh *.bex);;"
                                                               "Zip files (*.zip);;"
                                                               "WAD files (*.wad);;"
                                                               "All files (*)")[0]
                try: newLastDir = (os.sep).join(files[-1].split("/")[:-1])
                except: pass
            for path in files:
                if path.endswith(".exe"):       # ignore ports dropped onto list
                    continue
                path = os.path.abspath(path).replace(os.path.abspath('.'), '.')   # check if relative path and save that instead
                item = QtWidgets.QListWidgetItem(path.split(os.sep)[-1])   # path.split(os.sep)[-1] -> filename from end of path
                item.setData(3, path)
                item.setCheckState(2)           # checked by default (2=checked 0=unchecked 1=partial)
                widget.addItem(item)

        ##### IWADS #####
        elif widget.objectName() == "iwadList":
            if files is None:
                files = QtWidgets.QFileDialog.getOpenFileNames(caption="Select one or more IWADs to add",
                                                            directory=self.lastDir,
                                                            filter="IWAD files (*.wad *.zip);;"
                                                            "WAD files (*.wad);;"
                                                            "Zip files (*.zip);;"
                                                            "All files (*)")[0]
                try: newLastDir = (os.sep).join(files[-1].split("/")[:-1])
                except: pass
            for path in files:
                if path.endswith(".exe"):       # ignore ports dropped onto list
                    continue
                # reads md5 hash of iwad to detect it, if auto detection is enabled
                if self.ui.bdlDetectIWADs.isChecked():
                    wadName, wadMaps = self.readWadMD5Hash(path, self.ui.bdlRejectBadIWADs.isChecked())
                else:   # guesses map list based on name of wad if auto detection is disabled
                    wadName, wadMaps = (path.split("/")[-1], self.guessWarpMapCombo(path.split("/")[-1].lower()))
                if wadName == 4194304:          # 4194304 -> bad iwad and cancel was selected
                    continue
                path = os.path.abspath(path).replace(os.path.abspath('.'), '.')
                item = QtWidgets.QListWidgetItem(wadName)
                item.setData(3, path)
                item.setData(4, wadMaps)
                widget.addItem(item)
                widget.setCurrentItem(item)

        ##### SOURCE PORTS #####
        elif widget.objectName() == "portCombo":
            if files is None:
                files = QtWidgets.QFileDialog.getOpenFileNames(caption="Select one or more source ports to add",
                                                            directory=self.lastDir,
                                                            filter="Executables (*.exe);;"
                                                            "All files (*)")[0]
                try: newLastDir = (os.sep).join(files[-1].split("/")[:-1])
                except: pass
            for path in files:
                if not path.endswith(".exe"):   # ignore NON-ports dropped onto dropdown
                    continue
                path = os.path.abspath(path).replace(os.path.abspath('.'), '.')
                widget.addItem(self.readPortName(path))
                widget.setItemData(widget.count()-1, path, 3)

        ##### DEMOS #####
        elif widget.objectName() == "demoRecordNameLineEdit":
            previousDemoName = widget.text().split(os.sep)[-1]
            demoDestination = QtWidgets.QFileDialog.getExistingDirectory(caption="Select a directory to save your demo",
                                                                        directory=self.lastDir)
            if demoDestination:     # check that a dir was actually picked, or else it will default to "."
                try:
                    newLastDir = demoDestination
                    widget.setText(os.path.abspath(demoDestination) + os.sep + previousDemoName)
                    widget.setText(os.path.abspath(demoDestination) + os.sep + previousDemoName)
                    self.ui.demoRecordRadio.setChecked(True)
                except:
                    widget.setText(os.path.abspath(demoDestination) + os.sep)

        elif widget.objectName() == "demoPlayPathLineEdit":
            if files is None:
                files = QtWidgets.QFileDialog.getOpenFileName(caption="Select a demo file to play",
                                                            directory=self.lastDir,
                                                            filter="Doom demo files (*.lmp);;"
                                                            "All files (*)")[0]
            if files:   # check that a file was actually picked, or else setText will empty the lineEdit
                try: newLastDir = (os.sep).join(files.split("/")[:-1])
                except Exception as error: print(error)
                try:
                    widget.setText(files)
                    self.ui.demoPlayRadio.setChecked(True)
                except: pass
        if not dragAndDropped:
            self.lastDir = newLastDir



    def addFileFromConfig(self, widget, path, name, warpStyle=0, checked=True):
        if os.path.exists(path):        # makes sure wad/port hasn't been misplaced
            if widget.objectName() == "pwadList":
                item = QtWidgets.QListWidgetItem(path.split(os.sep)[-1])
                item.setData(3, path)
                item.setCheckState(QtCore.Qt.Checked if checked else QtCore.Qt.Unchecked)
                widget.addItem(item)
            elif widget.objectName() == "iwadList":
                item = QtWidgets.QListWidgetItem(name)
                item.setData(3, path)
                try: item.setData(4, mapNumberStyles[int(warpStyle)])
                except: item.setData(4, None)
                widget.addItem(item)
                widget.setCurrentItem(item)
            elif widget.objectName() == "portCombo":
                widget.addItem(name)
                widget.setItemData(widget.count()-1, path, 3)



    def showPopup(self, title, text, textInformative=None, textDetailed=None, textDetailedAutoOpen=False,
                buttons=QMessageBox.Ok, defaultButton=QMessageBox.Ok, icon=QMessageBox.Warning, modal=0):
        if not text:    # kills popup if no text is passed
            return
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        if textInformative: msg.setInformativeText(textInformative)
        if textDetailed: msg.setDetailedText(textDetailed)
        msg.setStandardButtons(buttons)
        msg.setDefaultButton(defaultButton)
        msg.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ui/BDL_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)    # allows copy/paste of popup text

        if textDetailedAutoOpen:        # auto-opens "Show Details..." button if present
            for button in msg.buttons():
                if button.text() == "Show Details...":
                    button.click()

        msg.setWindowModality(modal)
        return msg.exec_()



####################################
##### -*- HELPER FUNCTIONS -*- #####
####################################



### Wad indentification functions ###
    # TODO: omgifol could be used MANY times here
    def readWadMD5Hash(self, wadToRead, rejectBadWads):      # wadToRead is the full path
        if os.stat(wadToRead).st_size < 29000000:      # 29mb limit (strife 27mb)
            with open(wadToRead, "rb") as wad:
                md5 = hashlib.md5(wad.read()).hexdigest()
            if md5 in iwadNames:
                try: return iwadNames[md5][0], iwadNames[md5][1]
                except: return iwadNames[md5][0], None
        if not rejectBadWads:
            return wadToRead.split("/")[-1], None

        response = self.showPopup(title="Invalid IWAD!",
                            text="Invalid and/or modified IWAD detected!",
                            textInformative="The following IWAD was not detected as a valid IWAD and\n"
                            "is either not a known IWAD or is modified in some way:\n\n"
                            + wadToRead.split("/")[-1] +
                            "\n\nIWADs are official game data files. They contain all of the\n"
                            "game's assets, and are used as the base for custom wads.\n"
                            "Examples: DOOM.WAD, DOOM2.WAD, TNT.WAD, etc.\n\n"
                            "If this is an unofficial IWAD or intentionally modified, press\n"
                            "OK to add it anyway. To disable this message, uncheck\n"
                            "the \"Warnings\" setting under the bdl tab.\n\n"
                            "You should never modify your IWADs.",
                            buttons=QMessageBox.Ok|QMessageBox.Cancel,
                            defaultButton=QMessageBox.Cancel)
        if response == 1024:
            return wadToRead.split("/")[-1], None
        else:
            return response, None


    def guessWarpMapCombo(self, wadName):
        # ONLY returns map list for filling the warp combo, doesn't return names yet
        if wadName in iwadNamesSimple:
            return iwadNamesSimple[wadName][1]
        return mapNumberStyles[4]   # invalid iwad, just assume Doom 2 style (MAP##)


    def fillWarpMapCombo(self, newWadItem, prevWadItem=None):
        # intentionally don't convert map nums to warp commands here ('E1M1' -> '1 1') for performance
        try:
            if not prevWadItem or prevWadItem.data(4) is not newWadItem.data(4):
                self.ui.warpMapCombo.clear()
                self.ui.warpMapCombo.addItem("")
                if newWadItem.data(4):
                    for mapNumber in newWadItem.data(4)[1:]:
                        self.ui.warpMapCombo.addItem(mapNumber)
        except: pass

        # TODO: currently unused to avoid importing omgifol
        #    for mapName in self.getWadMapList(self.ui.iwadList.currentItem().data(3)):
        #        self.ui.warpMapCombo.addItem(mapName)
        #def getWadMapList(self, path):
        #    try:
        #        wad = omg.WAD(path)
        #        for mapName in wad.maps:
        #            yield mapName
        #    except: pass



### Port functions ###
    def readPortName(self, portToRead):
        port = portToRead.split(os.sep)[-1]
        if port in portNames:
            return portNames[port]
        return port


    def renamePort(self):
        if not self.ui.portRenameLineEdit.isVisible():     # rename started
            self.ui.portRenameLineEdit.show()      # show lineEdit to rename
            self.ui.portRenameLineEdit.setText(self.ui.portCombo.currentText())   # start with original name
            self.ui.portRenameLineEdit.selectAll()     # start with text selected
            self.ui.portRenameLineEdit.setFocus(QtCore.Qt.NoFocusReason)   # grab focus to type immediately
        else:   # rename finished
            newName = self.ui.portRenameLineEdit.text()
            if newName:  # if the lineEdit is blank, don't change the name
                self.ui.portCombo.setItemText(self.ui.portCombo.currentIndex(), newName)   # change name
            self.ui.portRenameLineEdit.hide()  # hide lineEdit


    def movePort(self, direction):
        try:
            portText = self.ui.portCombo.currentText()
            portData = self.ui.portCombo.currentData(3)
            portIndex = self.ui.portCombo.currentIndex()
            newIndex = 0

            if direction == "up":       newIndex = portIndex - 1
            elif direction == "down":   newIndex = portIndex + 1
            elif direction == "top":    newIndex = 0
            elif direction == "bottom": newIndex = self.ui.portCombo.count() - 1

            self.ui.portCombo.removeItem(portIndex)
            self.ui.portCombo.insertItem(newIndex, portText)
            self.ui.portCombo.setItemData(newIndex, portData, 3)
            self.ui.portCombo.setCurrentIndex(newIndex)
        except: pass



### ListWidget functions ###
    def getListWidgetItems(self, listWidget):
        for i in range(listWidget.count()):
            yield listWidget.item(i)


    def removeListItem(self, listWidget):
        selected = list(listWidget.row(item) for item in listWidget.selectedItems())  # list of currently selected item indexes
        selected.sort(reverse=True)                  # sorts list to delete higher indexes first to avoid indexes being updated
        for index in selected:         # uses takeItem() to remove items and deletes them manually since qt won't do it for you
            garbage = listWidget.takeItem(index)
            del garbage



### ListWidgetItem functions ###
    def resetPWADsCheckable(self):
        if self.ui.bdlPWADsCheckable.isChecked():
            self.ui.pwadList.setStyleSheet("QListWidget { outline: 0; }\n"
                                        "QListWidget::indicator {\n"
                                        "width: 8px;\n"
                                        "height: 8px;\n"
                                        "right: -4px; }\n"
                                        "QListView::item:text {\n"
                                        "color: black;\n"
                                        "padding-left: -5px;\n"
                                        "padding-top: -1px; }\n"
                                        "QListWidget::indicator::checked {\n"
                                        "image: url(:/ui/checkbox_on6.png); }\n"
                                        "QListWidget::item { margin-left: 0px; }")
        else:
            self.ui.pwadList.setStyleSheet("QListWidget { outline: 0; }\n"
                                        "QListWidget::indicator {\n"
                                        "width: 8px;\n"
                                        "height: 8px;\n"
                                        "right: -4px; }\n"
                                        "QListView::item:text {\n"
                                        "color: black;\n"
                                        "padding-left: -5px;\n"
                                        "padding-top: -1px; }\n"
                                        "QListWidget::indicator::checked {\n"
                                        "image: url(:/ui/checkbox_on6.png); }\n"
                                        "QListWidget::item { margin-left: -10px; }")


    def resetIWADFlags(self):   # Workaround for Qt bug in which dragging resets list item flags.
        try:
            self.ui.iwadList.currentItem().setFlags(QtCore.Qt.ItemIsSelectable|
                                                 QtCore.Qt.ItemIsEditable|
                                                 QtCore.Qt.ItemIsDragEnabled|
                                                 QtCore.Qt.ItemIsEnabled)
        except: pass        # Try-except block to prevent crash with no iwads



### Clear functions ###
    def clearEverything(self):
        response = self.showPopup(title='Are you sure?',
                                  text='Are you sure? This will clear all\n'
                                  'of your PWADs, IWADs, and source ports.',
                                  buttons=QMessageBox.Ok|QMessageBox.Cancel,
                                  icon=QMessageBox.Information)
        if response == 1024:
            self.clearListWidgetItems(self.ui.pwadList)
            self.clearListWidgetItems(self.ui.iwadList)
            self.clearPorts(showWarning=False)

    def clearListWidgetItems(self, listWidget):
        # getListWidgetItems yields items, so we'll put them into a separate list.
        toRemove = [item for item in self.getListWidgetItems(listWidget)]
        for item in toRemove:
            item.setSelected(True)
            self.removeListItem(listWidget)

    def clearPorts(self, showWarning=True):
        if showWarning:
            response = self.showPopup(title='Are you sure?',
                                      text='Are you sure? This will clear all of your source ports.',
                                      buttons=QMessageBox.Ok|QMessageBox.Cancel,
                                      icon=QMessageBox.Information)
        if not showWarning or response == 1024:
            while self.ui.portCombo.currentIndex() != -1:
                self.ui.portCombo.removeItem(self.ui.portCombo.currentIndex())



### Misc functions ###
    def autoRecordTimeout(self):
        if isinstance(self.autoRecordProcess, subprocess.Popen) and self.autoRecordProcess.poll() is not None:
            self.autoRecordTimer.stop()
            if self.isRecordingDemo():
                self.autoRecordDemoAttempt += 1
                self.prepareLaunch()
            else:   # stop autorecorder
                self.autoRecordDemoAttempt = 1
                self.autoRecordDemoSession = 1


    def isRecordingDemo(self):
        return (self.ui.demoAutoRecordCheck.isChecked() and self.ui.demoAutoRecordCheck.isEnabled() and self.ui.demoGroup.isChecked() and self.ui.demoRecordRadio.isChecked())


    def changeDoomCapitalization(self):
        if self.ui.bdlCapitalization.isChecked():
            capsStyle = self.ui.bdlCapitalizationCombo.currentText()
            for iwad in self.getListWidgetItems(self.ui.iwadList):
                try:
                    oldName = iwad.text()
                    nameIndex = oldName.lower().find("doom")
                    if nameIndex != -1:
                        iwad.setText(oldName[:nameIndex] + capsStyle + oldName[nameIndex+4:])
                except: continue


    def saveCustomConfig(self):
        file = QtWidgets.QFileDialog.getSaveFileName(caption="Save configuration",
                                                     directory=self.lastDir,
                                                     filter="ini (*.ini);;"
                                                     "cfg (*.cfg);;"
                                                     "All files (*)")[0]
        self.lastDir = (os.sep).join(file.split("/")[:-1])
        config.saveConfig(self, file)


    def loadCustomConfig(self):
        file = QtWidgets.QFileDialog.getOpenFileName(caption="Select configuration to load",
                                                     directory=self.lastDir,
                                                     filter="BDL config files (*.ini);;"
                                                     "Other config files (*.bdl *.cfg);;"
                                                     "All files (*)")[0]
        try: self.lastDir = (os.sep).join(file.split("/")[:-1])
        except: pass
        config.loadConfig(self, file)


    def openAboutDialog(self):
        aboutDialog = QtWidgets.QDialog()
        aboutDialog.setWindowModality(1)
        aboutUi = window_about.Ui_aboutDialog()
        aboutUi.setupUi(aboutDialog)
        aboutDialog.exec()



bdl = BDLInstance()     # create empty bdl instance



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BDLMainWindow = QtWidgets.QMainWindow()
    ui = window_main.Ui_BDLMainWindow()
    ui.setupUi(BDLMainWindow)
    bdl.setupBDL(ui, BDLMainWindow)     # setup bdl instance
    BDLMainWindow.show()
    response = app.exec_()
    config.saveConfig(bdl)              # save config on exit
    sys.exit(response)