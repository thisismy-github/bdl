# Collection of Qt widgets subclassed for use in BDL.
from PyQt5.QtWidgets import QListWidget, QComboBox, QLineEdit



# Hacky solution to allow custom widgets to interface with bdl.py
bdlInstance = None
def setBDLInstance(newBDLInstance):
    global bdlInstance
    bdlInstance = newBDLInstance



class bdlListWidget(QListWidget):
    '''
    Custom QListWidget class that allows external file drag-and-drop.
    Actual event functions were taken from this github example,
    since figuring this out normally was essentially impossible:
    https://gist.github.com/peace098beat/db8ef7161508e6500ebe
    Used for the iwad and pwad lists.
    '''
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
        super().dragEnterEvent(event)   # run QListWidget's built-in behavior

    def dropEvent(self, event):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        bdlInstance.addFile(self, files, dragAndDropped=True)
        super().dropEvent(event)        # run QListWidget's built-in behavior



class bdlComboBox(QComboBox):
    '''
    Custom QComboBox (dropdown) class that allows external
    file drag-and-drop. Used for the source port dropdown.
    '''
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        bdlInstance.addFile(self, files, dragAndDropped=True)



class bdlDemoLineEdit(QLineEdit):
    '''
    Custom QLineEdit class that allows external file drag-and-drop.
    This version is explicitly designed to allow Doom demo (.lmp) files
    only. Used for the "Play Demo" line edit under the settings tab.
    '''
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            path = event.mimeData().urls()[0].toLocalFile()   # only accept demo files (.lmp)
            if path.endswith('.lmp'): event.accept()
            else: event.ignore()
        else:
            event.ignore()

    def dropEvent(self, event):
        bdlInstance.addFile(self, files=event.mimeData().urls()[0].toLocalFile(), dragAndDropped=True)