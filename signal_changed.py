from PyQt5.QtCore import QObject, pyqtSignal


class SignalChanged(QObject):
    sigchr = pyqtSignal(list)

    def __init__(self):
        QObject.__init__(self)
