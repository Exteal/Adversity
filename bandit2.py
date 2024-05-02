from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QHBoxLayout, QFrame, QApplication
from PyQt5.QtCore import QObject, pyqtSignal

import WidgetSlotMachine as SlotM
import time
import random

class BanditClickedEmitter(QObject):
    custom_signal = pyqtSignal()

class BanditClickedReceiver(QObject):
    custom_signal = pyqtSignal()


class BanditWidget(QFrame):
    def __init__(self, rewards, apriori):
        super().__init__()
        self.rewards = rewards
        self.apriori = apriori
        self.score = 0

        self.banditClickedEmitter = BanditClickedEmitter()
        self.banditClickedReceiver = BanditClickedReceiver()

        self.banditClickedReceiver.custom_signal.connect(self.receiveClicked)

        self.setGeometry(0, 0, 408, 476)
        self.ui = SlotM.Ui_Form()
        self.ui.setupUi(self)
        self.cpt = 0


        self.spining = False
        self.ui.pushButton.released.connect(self.spin)

    def spin(self):
        self.spining = True
        self.ui.pushButton.setDisabled(True)
        for i in range(0, 20):
            time.sleep((50 + 25 * i) / 10000)

            self.ui.reward.setProperty("intValue", random.randint(0, 9999))
            
            QApplication.processEvents()

        self.cpt += 1
        print(str(self.rewards))
        self.score = self.score + self.rewards[0]
        self.ui.reward.setProperty("intValue", self.rewards[0])
        self.ui.score.setProperty("intValue", self.score)

        # if a == b and c == b:
        #     print("===============")
        #     print("=== JACKPOT ===")
        #     print("===============")

        # else:
        #     print("game over, " + str(self.cpt) + " games played")
        self.spining = False
        self.ui.pushButton.setDisabled(False)
        self.banditClickedEmitter.custom_signal.emit()

        

    def receiveClicked(self):
        print(self.rewards)
        #self.apriori = str(self.rewards[0]) + "\n" + self.apriori
        self.rewards.pop(0)
        
        # if len(self.rewards) == 0:
        #     self.ui.pushButton.setEnabled(False)
        #     self.ui.pushButton.setDisabled(True)
            #self.aprioriWidget.setText("Fin de la partie")
            

