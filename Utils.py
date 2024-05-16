from PyQt5.QtCore import pyqtSignal, QObject
from enum import StrEnum
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout


# La valeur None fait aparaître le sélecteur de dossier à l'ouverture de l'application
# Pour éviter cela, cette variable prednra la forme d'une chaîne de caractères menant vers le dossier contenant les fichiers utilisateur.  
user_files_directory = None

# Le chemin vers le dossier qui contiendra les fichiers csv de log crées par l'application.
log_directory = "logs/"


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

       