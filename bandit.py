#from PyQt5.QtGui import QKeyEvent, QMouseEvent, QCursor
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal

class BanditClickedEmitter(QObject):
    custom_signal = pyqtSignal()

class BanditClickedReceiver(QObject):
    custom_signal = pyqtSignal()

class BanditWidget(QWidget):
    def __init__(self, rewards, apriori):
        super().__init__()
        self.rewards = rewards
        self.apriori = apriori
        self.score = 0

        self.banditClickedEmitter = BanditClickedEmitter()
        self.banditClickedReceiver = BanditClickedReceiver()

        self.banditClickedReceiver.custom_signal.connect(self.receiveClicked)
        self.initUi()
    

    def initUi(self):
        self.button = QPushButton(self)
        self.button.clicked.connect(self.emitClicked)
        self.aprioriWidget = QTextEdit(self)
        self.aprioriWidget.setReadOnly(True)
        self.aprioriWidget.setText(self.apriori)

        layout = QHBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.aprioriWidget)


    def emitClicked(self):
        self.score = self.score + self.rewards[0]
        self.banditClickedEmitter.custom_signal.emit()

    def receiveClicked(self):
        print(self.rewards)
        self.rewards.pop(0)

    #def painEvent(self, event):

