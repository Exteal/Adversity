from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget, QTextEdit, QPushButton, QHBoxLayout, QFrame, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QObject, pyqtSignal, Qt

from bandit2 import BanditWidget


class BanditFinishedEmitter(QObject):
    custom_signal = pyqtSignal()




class InterfaceBandit(QMainWindow):
    def __init__(self, bras):
        super().__init__()
        self.log_file =  open("log_recommandations.csv", "w", newline='')
        if bras[0]["side"] == "gauche":
            self.initUi(bras[0], bras[1])
        
        else :
            self.initUi(bras[1], bras[0])


    def initUi(self, leftArm, rightArm):
        
        self.banditFinishedEmitter = BanditFinishedEmitter()

        self.tentatives = leftArm["rewards"].__len__()
        # attributs de la fenetre principale
        self.showMaximized()
        #self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Slot Machine')
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout_all = QVBoxLayout()
        
        layout = QHBoxLayout()
        ##############################
        self.mLeft = BanditWidget(leftArm["rewards"], leftArm["a priori"])
        ###############
        center_layout = QVBoxLayout()
        center_layout.setAlignment(Qt.AlignHCenter)
        ###############
        self.nb_tentatives = QLabel(self)
        self.nb_tentatives.setAlignment(Qt.AlignCenter)
        font = self.nb_tentatives.font()
        font.setPointSize(20)
        self.nb_tentatives.setFont(font)
        self.nb_tentatives.setText("Nombre de tentatives restantes : " + str(self.tentatives))
        #####
        self.scoreWidget = QLabel(self)
        self.scoreWidget.setAlignment(Qt.AlignCenter)
        fontS = self.scoreWidget.font()
        fontS.setPointSize(40)
        self.scoreWidget.setFont(fontS)
        self.scoreWidget.setText("Score Total : 0")
        ###############
        self.mRight = BanditWidget(rightArm["rewards"], rightArm["a priori"])
        ##############################
        center_layout.addWidget(self.nb_tentatives)
        center_layout.addWidget(self.scoreWidget)
        layout.addWidget(self.mLeft)
        layout.addLayout(center_layout)
        layout.addWidget(self.mRight)
        layout.setAlignment(Qt.AlignCenter)
        
        objectif = QLabel(self)
        objectif.setAlignment(Qt.AlignCenter)
        font = objectif.font()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        objectif.setFont(font)
        objectif.setStyleSheet("QLabel { color : #EE0000; }")
        objectif.setText("Objectif : Vous devez choisir le bras qui rapporte le plus de points en " + str(self.tentatives) + " tentatives")
        layout_all.addWidget(objectif)
        layout_all.addLayout(layout)
        central_widget.setLayout(layout_all)

        self.mLeft.banditClickedEmitter.custom_signal.connect(lambda: self.onclickedSpin())
        self.mRight.banditClickedEmitter.custom_signal.connect(lambda: self.onclickedSpin())
        
        #self.score = self.mLeft.score + self.mRight.score

    # def keyPressEvent(self, e):
    #     if e.key() == QtCore.Qt.Key_Left and not self.mLeft.spining and not self.mRight.spining:
    #         self.mLeft.spin()
    #     if e.key() == QtCore.Qt.Key_Right and not self.mRight.spining and not self.mRight.spining:
    #         self.mRight.spin()
    
    
    
    def onClickedEnd(self, event):
        self.banditFinishedEmitter.custom_signal.emit()
        self.log_file.close()
    
    def onclickedSpin(self):
       
        score = self.mLeft.score + self.mRight.score
        self.tentatives -= 1
        self.scoreWidget.setText("Score Total : " + str(score))
        self.nb_tentatives.setText("Nombre de tentatives restantes : " + str(self.tentatives))
        if self.tentatives == 0:
            self.mLeft.ui.pushButton.setEnabled(False)
            self.mLeft.ui.pushButton.setDisabled(True)
            self.mRight.ui.pushButton.setEnabled(False)
            self.mRight.ui.pushButton.setDisabled(True)

            wid = self.centralWidget()
            wid.mouseReleaseEvent = self.onClickedEnd

            
        self.mLeft.banditClickedReceiver.custom_signal.emit()
        self.mRight.banditClickedReceiver.custom_signal.emit()