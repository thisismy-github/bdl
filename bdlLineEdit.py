from PyQt5 import QtCore, QtGui, QtWidgets
import run

class bdlLineEdit(QtWidgets.QLineEdit):
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
        run.addFile(self, files=event.mimeData().urls()[0].toLocalFile())