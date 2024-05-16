from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QHBoxLayout
from Styles import endPageButtonStyle
import sys


class EndPageWidget(QMainWindow):
    def __init__(self, stack):
        super().__init__()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)



        main_layout = QHBoxLayout(central_widget)

        self.bparams = QPushButton("Retour sélection participant")
        self.bparams.clicked.connect(lambda : returnParams(stack))

        self.bend = QPushButton("Fermer l'appli")
        self.bend.clicked.connect(lambda : quitApp())

        self.bparams.setFixedHeight(300)
        self.bend.setFixedHeight(300) 

        self.bparams.setStyleSheet(endPageButtonStyle)
        self.bend.setStyleSheet(endPageButtonStyle)

        main_layout.addWidget(self.bparams)
        main_layout.addWidget(self.bend)




def returnParams(stack):
    for idx in reversed(range(1, stack.count() - 1)):
        widget = stack.widget(idx)
        stack.removeWidget(widget)
        widget.deleteLater()
    
    stack.widget(0).deselect_all()
    stack.setCurrentIndex(0)

def quitApp():
    sys.exit()