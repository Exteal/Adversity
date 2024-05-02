from PyQt5.QtCore import pyqtSignal, QObject
from enum import StrEnum


class NextPageEmitter(QObject):
    custom_signal = pyqtSignal()

class Types(StrEnum):
    RECOMMANDATION = "recommandation"
    BANDIT = "bandit"  