from PyQt5 import QtCore, QtGui, QtWidgets
import run

class bdlComboBox(QtWidgets.QComboBox):
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
        run.addFile(self, files)