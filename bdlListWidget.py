from PyQt5 import QtCore, QtGui, QtWidgets
import run

class bdlListWidget(QtWidgets.QListWidget):
    # Custom QListWidget class that allows dragging and dropping external files onto it.
    # "layout" is a parameter that isn't listed in the documentation
    # nor any error messages, yet is required for the widget to run.
    # Actual event functions were taken from this github example, since figuring this out
    # normally was practically impossible: https://gist.github.com/peace098beat/db8ef7161508e6500ebe
    def __init__(self, parent, fileType):
        super().__init__(parent)
        self.type = fileType
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
        super().dragEnterEvent(event)

    def dropEvent(self, event):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        run.addFile(self, files)
        super().dropEvent(event)