from PyQt5.QtCore import pyqtSignal, QObject
from enum import StrEnum
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QSizePolicy


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import * 

from PyQt5.QtCore import Qt



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
            self.showMaximized()

        def paintEvent(self, event):
            painter = QPainter(self)
            
            pen = QPen()
            brush = QBrush()

            
            font = QFont("Verdana")
            font.setPointSize(font.pointSize() * 2)
          #  pen.setStyle(Qt.PenStyle.DashDotLine)
           # pen.setWidth(25)
            
            painter.setFont(font)
            brush.setColor(QColor("black"))
            width,height = self.size().width(), self.size().height()

            fontsizes = font.pointSize()
            painter.setPen(pen)
            painter.setBrush(brush)

            
            painter.drawText(QRectF(0, 0, width, height),Qt.AlignmentFlag.AlignCenter,"Cliquez n'importe où pour passer au block suivant")
        
