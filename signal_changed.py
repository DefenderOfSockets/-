from PyQt5 import QtCore


class SignalChanged(QtCore.QObject):
    sigchr = QtCore.pyqtSignal(list)

    def __init__(self):
        QtCore.QObject.__init__(self)