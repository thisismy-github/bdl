# Runs final command line to play DOOM with selected settings.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os, subprocess, hashlib, shutil, platform, collections, configparser
from names import portNames, iwadNames
import time

# TODO: add full auto-sort for ports+iwads
# TODO: add fallback for empty wad/port names

bdlAutoDetectIWADs = True
bdlRejectBadIWADs = True

def run(port, iwad, complevel=None, pwads=None, deh=None,
        settings=None, extra=None, noLaunch=False):
    # TODO: add relative path variant?
    command = '"' + os.path.abspath(port) + '"'  # intentionally different -> missing port causes TypeError here
    command += f" -iwad {os.path.abspath(iwad)}"
    if pwads: command += f" -file {pwads}"
    if deh: command += f" -deh {deh}"
    if complevel: command += f" {complevel}"
    if settings: command += f" {settings}"
    if extra: command += f" {extra}"

    if not noLaunch: return subprocess.Popen(command)  # Popen prevents bdl from hanging while game is open
    return command



def showPopup(title, text, textInformative=None, textDetailed=None, textDetailedAutoOpen=False,
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

    if textDetailedAutoOpen:        # automatically opens "Show Details..." button if present
        for button in msg.buttons():
            if button.text() == "Show Details...":
                button.click()

    msg.setWindowModality(modal)
    return msg.exec_()



def updateBDLSettings(autoDetect, reject):
    # hacky solution to allow bdlAutoDetectIWADs and bdlRejectBadIWADs
    # to work with both the ui buttons AND drag and dropping files
    global bdlAutoDetectIWADs
    global bdlRejectBadIWADs
    bdlAutoDetectIWADs = autoDetect
    bdlRejectBadIWADs = reject



def findSteamIWADs(widget):
    # TODO: add heretic, hexen, strife
    # TODO: move 64-bit check + OS check to ini file
    # TODO: cross-platform support
    currentOS = platform.system()
    is64bit = platform.machine().endswith("64")

    if currentOS is not 'Windows':  # don't even bother if not on windows, this won't work yet
        return

    # 64/32-bit Windows paths to each of the main Doom IWADs
    programFilesDir = "%PROGRAMFILES(X86)%" if is64bit else "%PROGRAMFILES%"
    steamIWADPaths = (programFilesDir + r"\Steam\steamapps\common\Ultimate Doom\base\DOOM.WAD",
                      programFilesDir + r"\Steam\steamapps\common\Doom 2\base\DOOM2.WAD",
                      programFilesDir + r"\Steam\steamapps\common\Final Doom\base\TNT.WAD",
                      programFilesDir + r"\Steam\steamapps\common\Final Doom\base\PLUTONIA.WAD",)

    try: os.mkdir(r".\IWADs")       # attempt to create IWADs directory
    except FileExistsError: pass

    # attempt to copy Master Levels wads to separate directory inside IWADs
    # NOTE: if the directory already exists and is not empty, no wads will be copied.
    if not os.path.isdir(r".\IWADs\Master Levels"):
        try: shutil.copytree(os.path.expandvars(programFilesDir + r"\Steam\steamapps\common\Master Levels of Doom\master\wads"),
                             r".\IWADs\Master Levels")
        except FileNotFoundError: pass

    for path in steamIWADPaths:         # attempts to find and copy each IWAD to IWADs folder
        wad = path.split("\\")[-1]      # wad's filename -> DOOM2.WAD, TNT.WAD, etc.
        if not os.path.exists(f".\\IWADs\\{wad}"):      # only copy if file is not present
            try: shutil.copy(os.path.expandvars(path), r".\IWADs")
            except: continue

    # TODO: master levels check
    # adds each found iwad to iwad list

    # if iwads not empty, sort .wad files from ultimate doom to plutonia, then add each
    iwadDir = os.listdir(r".\IWADs")
    if iwadDir:
        # create list of absolute paths to each file in .\IWADs that ends in .wad (to ignore Master Levels)
        files = list(os.path.abspath(r".\IWADs") + "\\" + file for file in iwadDir if file.lower().endswith(".wad"))
        sortedFiles = []
        wadPriority = ('DOOM.WAD', 'DOOM2.WAD', 'TNT.WAD', 'PLUTONIA.WAD')
        for wad in wadPriority:
            wadPath = os.path.abspath(r".\IWADs") + "\\" + wad
            if wadPath in files:
                sortedFiles.append(wadPath)
        addFile(widget, sortedFiles)
    else:
        os.rmdir(r".\IWADs")    # delete directory if it's empty
    widget.setCurrentRow(0)     # selects first iwad (usually ultimate doom)



def readWadMD5Hash(wadToRead, reject):      # wadToRead is the full path
    if os.stat(wadToRead).st_size < 29000000:      # 28mb limit (strife 27mb)
        with open(wadToRead, "rb") as wad:
            md5 = hashlib.md5(wad.read()).hexdigest()
        if md5 in iwadNames:
            return iwadNames[md5][0]
    if not reject:
        return wadToRead.split("/")[-1]

    response = showPopup(title="Invalid IWAD!",
                         text="Invalid and/or modified IWAD detected!",
                         textInformative="The following IWAD was not detected as a valid IWAD and\n"
                         "is either not a known IWAD or is modified in some way:\n\n"
                         + wadToRead.split("/")[-1] +
                         "\n\nIWADs are official game data files. They contain all of the\n"
                         "game's assets, and are used as the base for custom wads.\n"
                         "Examples: DOOM.WAD, DOOM2.WAD, TNT.WAD, etc.\n\n"
                         "If this is an unofficial IWAD or intentionally modified, press\n"
                         "OK to add it anyway. To disable this message, uncheck\n"
                         "the \"Automatically detect IWADs\" setting under the bdl tab.\n\n"
                         "You should never modify your IWADs.",
                         buttons=QMessageBox.Ok|QMessageBox.Cancel,
                         defaultButton=QMessageBox.Cancel)
    if response == 1024:
        return wadToRead.split("/")[-1]
    else:
        return response



def readPortName(portToRead):
    port = portToRead.split("/")[-1]
    if port in portNames:
        return portNames[port]
    return port



# TODO: oh gosh none of this will work outside windows will it
def addFile(widget, files=None, lastDir=None):
    global bdlAutoDetectIWADs   # part of the hacky solution mentioned
    global bdlRejectBadIWADs    # above in updateBDLSettings()
    newLastDir = lastDir
    ##### PWADS #####
    if widget.objectName() == "pwadList":
        if files is None:
            files = QtWidgets.QFileDialog.getOpenFileNames(caption="Select one or more files to add",
                                                           directory=lastDir,
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
            if path.endswith(".exe"):                               # ignore ports dropped onto list
                continue
            item = QtWidgets.QListWidgetItem(path.split("/")[-1])   # path.split('/')[-1] returns the filename after the last / in a path.
            item.setData(3, path)
            item.setCheckState(QtCore.Qt.Checked)                   # checked by default (2=checked 0=unchecked 1=partial)
            widget.addItem(item)

    ##### IWADS #####
    elif widget.objectName() == "iwadList":
        if files is None:
            files = QtWidgets.QFileDialog.getOpenFileNames(caption="Select one or more IWADs to add",
                                                           directory=lastDir,
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
            wadName = readWadMD5Hash(path, bdlRejectBadIWADs) if bdlAutoDetectIWADs else path.split("/")[-1]
            if wadName == 4194304:          # 4194304 -> bad iwad and cancel was selected
                continue
            item = QtWidgets.QListWidgetItem(wadName)
            item.setData(3, path)
            widget.addItem(item)
            widget.setCurrentItem(item)

    ##### SOURCE PORTS #####
    elif widget.objectName() == "portCombo":
        if files is None:
            files = QtWidgets.QFileDialog.getOpenFileNames(caption="Select one or more source ports to add",
                                                           directory=lastDir,
                                                           filter="Executables (*.exe);;"
                                                           "All files (*)")[0]
            try: newLastDir = (os.sep).join(files[-1].split("/")[:-1])
            except: pass
        for path in files:
            if not path.endswith(".exe"):   # ignore NON-ports dropped onto dropdown
                continue
            widget.addItem(readPortName(path))
            widget.setItemData(widget.count()-1, path, 3)

    ##### DEMOS #####
    elif widget.objectName() == "demoRecordNameLineEdit":
        previousDemoName = widget.text().split(os.sep)[-1]
        demoDestination = QtWidgets.QFileDialog.getExistingDirectory(caption="Select a directory to save your demo",
                                                                     directory=lastDir)
        if demoDestination:     # check that a dir was actually picked, or else it will default to "."
            try:
                newLastDir = demoDestination
                widget.setText(os.path.abspath(demoDestination) + os.sep + previousDemoName)
                widget.setText(os.path.abspath(demoDestination) + os.sep + previousDemoName)
            except:
                widget.setText(os.path.abspath(demoDestination) + os.sep)

    elif widget.objectName() == "demoPlayPathLineEdit":
        if files is None:
            files = QtWidgets.QFileDialog.getOpenFileName(caption="Select a demo file to play",
                                                          directory=lastDir,
                                                          filter="Doom demo files (*.lmp);;"
                                                          "All files (*)")[0]
        try: newLastDir = (os.sep).join(files.split("/")[:-1])
        except: pass
        if files:   # check that a file was actually picked, or else setText will empty the lineEdit
            try: widget.setText(files)
            except: pass
    return newLastDir



def addFileFromConfig(widget, path, name, checked=True):
    if os.path.exists(path):        # makes sure wad/port hasn't been misplaced
        if widget.objectName() == "pwadList":
            item = QtWidgets.QListWidgetItem(path.split("/")[-1])
            item.setData(3, path)
            item.setCheckState(QtCore.Qt.Checked if checked else QtCore.Qt.Unchecked)
            widget.addItem(item)
        elif widget.objectName() == "iwadList":
            item = QtWidgets.QListWidgetItem(name)
            item.setData(3, path)
            widget.addItem(item)
            widget.setCurrentItem(item)
        elif widget.objectName() == "portCombo":
            widget.addItem(name)
            widget.setItemData(widget.count()-1, path, 3)