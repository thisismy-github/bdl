# Runs final command line to play DOOM with selected settings.

from PyQt5 import QtCore, QtGui, QtWidgets
import os, hashlib

def run(port, iwad, complevel, pwads=None, deh=None, warp=0, skill=0, extra=None):
    command = port
    command += f" -iwad {iwad}"
    if pwads: command += f" -file {pwads}"
    if deh: command += f" -deh {deh}"
    if warp: command += f" -warp {warp}"
    if skill: command += f" -skill {skill}"
    command += " " + complevel
    if extra: command += " " + extra

    print(command)
    os.system(command)

def addFile(widget, files=None):
    ##### PWADS #####
    if widget.type == 'pwad':
        if files is None:
            files = QtWidgets.QFileDialog.getOpenFileNames(caption="Select one or more files to add",
                                                           filter="DOOM files (*.wad *.zip *.deh *.bex *.pk3 *.pk7 *.pkz *.ipk7 *p7z);;"
                                                           "Vanilla Doom files (*.wad *.zip *.deh);;"
                                                           "Boom files (*.wad *.zip *.deh *.bex);;"
                                                           "ZDoom files (*.pk3 *.pk7 *.pkz *.ipk7 *p7z);;"
                                                           "Patch files (*.deh *.bex);;"
                                                           "Zip files (*.zip);;"
                                                           "WAD files (*.wad);;"
                                                           "All files (*)")[0]
        for path in files:
            if path.endswith('.exe'):
                continue
            item = QtWidgets.QListWidgetItem(path.split('/')[-1])       # path.split('/')[-1] returns the filename after the last / in a path.
            item.setData(3, path)
            item.setCheckState(QtCore.Qt.Checked)                       # checked by default
            widget.addItem(item)
    ##### IWADS #####
    elif widget.type == 'iwad':
        if files is None:
            files = QtWidgets.QFileDialog.getOpenFileNames(caption="Select one or more IWADs to add",
                                                           filter="IWAD files (*.wad *.zip);;"
                                                           "WAD files (*.wad);;"
                                                           "Zip files (*.zip);;"
                                                           "All files (*)")[0]
        for path in files:
            if path.endswith('.exe'):
                continue
            item = QtWidgets.QListWidgetItem(path.split('/')[-1])
            item.setData(3, path)
            widget.addItem(item)
    ##### SOURCE PORTS #####
    elif widget.type == 'port':
        if files is None:
            files = QtWidgets.QFileDialog.getOpenFileNames(caption="Select one or more source ports to add",
                                                           filter="Executables (*.exe);;"
                                                           "All files (*)")[0]
        for path in files:
            if not path.endswith('.exe'):
                continue
            widget.addItem(path.split('/')[-1])              # TODO add auto-naming system
            widget.setItemData(widget.count()-1, path, 3)






# steps to recreate file:
# change QtWidgets.QListWidget to QListWidgetDroppable
# change QtWidgets.QComboBox to QComboBoxDroppable
# add fileType parameter to each -> 'iwad', 'pwad', 'port'

#def addFile(widget, files=None):
#    ##### PWADS #####
#    if widget.type == 'pwad':
#        if files is None:
#            files = QtWidgets.QFileDialog.getOpenFileNames(caption="Select one or more files to add",
#                                                           filter="DOOM files (*.wad *.zip *.deh *.bex *.pk3 *.pk7 *.pkz *.ipk7 *p7z);;"
#                                                           "Vanilla Doom files (*.wad *.zip *.deh);;"
#                                                           "Boom files (*.wad *.zip *.deh *.bex);;"
#                                                           "ZDoom files (*.pk3 *.pk7 *.pkz *.ipk7 *p7z);;"
#                                                           "Patch files (*.deh *.bex);;"
#                                                           "Zip files (*.zip);;"
#                                                           "WAD files (*.wad);;"
#                                                           "All files (*)")[0]
#        for path in files:
#            if path.endswith('.exe'):
#                continue
#            item = QtWidgets.QListWidgetItem(path.split('/')[-1])       # path.split('/')[-1] returns the filename after the last / in a path.
#            item.setData(3, path)
#            item.setCheckState(QtCore.Qt.Checked)                       # checked by default
#            widget.addItem(item)
#    ##### IWADS #####
#    elif widget.type == 'iwad':
#        if files is None:
#            files = QtWidgets.QFileDialog.getOpenFileNames(caption="Select one or more IWADs to add",
#                                                           filter="IWAD files (*.wad *.zip);;"
#                                                           "WAD files (*.wad);;"
#                                                           "Zip files (*.zip);;"
#                                                           "All files (*)")[0]
#        for path in files:
#            if path.endswith('.exe'):
#                continue
#            item = QtWidgets.QListWidgetItem(path.split('/')[-1])
#            item.setData(3, path)
#            widget.addItem(item)
#    ##### SOURCE PORTS #####
#    elif widget.type == 'port':
#        if files is None:
#            files = QtWidgets.QFileDialog.getOpenFileNames(caption="Select one or more source ports to add",
#                                                           filter="Executables (*.exe);;"
#                                                           "All files (*)")[0]
#        for path in files:
#            if not path.endswith('.exe'):
#                continue
#            widget.addItem(path.split('/')[-1])              # TODO add auto-naming system
#            widget.setItemData(widget.count()-1, path, 3)
#
#
#class QListWidgetDroppable(QtWidgets.QListWidget):
#    # Custom QLIstWidget class that allows dragging and dropping external files onto it.
#    # "layout" is a parameter that isn't listed in the documentation
#    # nor any error messages, yet is required for the widget to run.
#    # Actual event functions were taken from this github example, since figuring this out
#    # normally was essentially impossible: https://gist.github.com/peace098beat/db8ef7161508e6500ebe
#    def __init__(self, layout, fileType):
#        super().__init__(layout)
#        self.type = fileType
#        self.setAcceptDrops(True)
#
#    def dragEnterEvent(self, event):
#        if event.mimeData().hasUrls():
#            event.accept()
#        else:
#            event.ignore()
#        super().dragEnterEvent(event)
#
#    def dropEvent(self, event):
#        files = [url.toLocalFile() for url in event.mimeData().urls()]
#        addFile(self, files)
#        super().dropEvent(event)
#
#class QComboBoxDroppable(QtWidgets.QComboBox):
#    def __init__(self, layout, fileType):
#        super().__init__(layout)
#        self.type = fileType
#        self.setAcceptDrops(True)
#
#    def dragEnterEvent(self, event):
#        if event.mimeData().hasUrls():
#            event.accept()
#        else:
#            event.ignore()
#
#    def dropEvent(self, event):
#        print([url.toLocalFile() for url in event.mimeData().urls()])
#        files = [url.toLocalFile() for url in event.mimeData().urls()]
#        addFile(self, files)