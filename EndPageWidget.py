from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QHBoxLayout
import sys


class EndPageWidget(QMainWindow):
    def __init__(self, stack):
        super().__init__()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()

        self.bparams = QPushButton("Retour sélection participant")
        self.bparams.clicked.connect(lambda : returnParams(stack))

        self.bend = QPushButton("Fermer l'appli")
        self.bend.clicked.connect(lambda : quitApp())

        main_layout.addWidget(self.bparams)
        main_layout.addWidget(self.bend)

        central_widget.setLayout(main_layout)    



def returnParams(stack):
    for idx in reversed(range(1, stack.count() - 1)):
        print(idx)
        widget = stack.widget(idx)
        stack.removeWidget(widget)
        widget.deleteLater()
    
    stack.widget(0).deselect_all()
    stack.setCurrentIndex(0)

def quitApp():
    sys.exit()