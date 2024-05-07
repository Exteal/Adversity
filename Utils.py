from PyQt5.QtCore import pyqtSignal, QObject
from enum import StrEnum
from PyQt5.QtWidgets import QLabel, QWidget

class NextPageEmitter(QObject):
    custom_signal = pyqtSignal()

class Types(StrEnum):
    RECOMMANDATION = "recommandation"
    BANDIT = "bandit"  


class WaitWidget(QWidget):
        def __init__(self):
            super().__init__()
            lab = QLabel(self)
            lab.setText("Passer au suivant")
            lab.setStyleSheet("color : #FFFFFF;")
            self.setStyleSheet("background-color : #000000;")
            self.showMaximized()

       