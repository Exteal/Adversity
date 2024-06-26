from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget, QTextEdit, QPushButton, QHBoxLayout, QFrame, QApplication, QLabel, QVBoxLayout, QDialog
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QObject, pyqtSignal, Qt

from bandit import BanditWidget

from questionnaire import QuestionnaireWidgetBandit
from Utils import NextPageEmitter, WaitWidget, log_directory

from time import sleep
import csv



class InterfaceBandit(QMainWindow):
    def __init__(self, bras, name, quest_countdown):
        super().__init__()
        self.log_file =  open(log_directory + "log_recommandations_" + name + ".csv", "w", newline='')
        self.log_quest = open(log_directory + "log_questionnaire_" + name + ".csv", "w", newline='')

        writer = csv.DictWriter(self.log_file, fieldnames=["choice"])
        writer.writeheader()
        
        self.questionnairecount = 0
        self.questionnaire_countdown = quest_countdown
        if bras[0]["side"] == "gauche":
            self.initUi(bras[0], bras[1])
        
        else :
            self.initUi(bras[1], bras[0])


    def initUi(self, leftArm, rightArm):
        
        self.nextPage = NextPageEmitter()

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
        self.mLeft = BanditWidget(leftArm["rewards"], leftArm["a priori"], self.log_file, "left")
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
        self.mRight = BanditWidget(rightArm["rewards"], rightArm["a priori"], self.log_file, "right")
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

    
    
    def show_questionnaire(self):
        
        # Créer une boîte de dialogue modale pour afficher le questionnaire
        dialog = QDialog(self)
        dialog.setWindowTitle("Questionnaire")
        dialog.setModal(True)

        # Créer le widget du questionnaire et ajouter à la boîte de dialogue
        questionnaire_widget = QuestionnaireWidgetBandit(self.log_quest)
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(questionnaire_widget)
        dialog.setLayout(dialog_layout)

        # Afficher la boîte de dialogue modale
        dialog.exec_()

    def onClickedEnd(self, event):
        self.nextPage.custom_signal.emit()
        self.log_file.close()
    
    def onclickedSpin(self):
       
        score = self.mLeft.score + self.mRight.score
        self.tentatives -= 1
        self.questionnairecount += 1


       

        self.scoreWidget.setText("Score Total : " + str(score))
        self.nb_tentatives.setText("Nombre de tentatives restantes : " + str(self.tentatives))
        if self.tentatives == 0:
           # sleep(2)
           # self.mLeft.ui.pushButton.setEnabled(False)
           # self.mLeft.ui.pushButton.setDisabled(True)
           # self.mRight.ui.pushButton.setEnabled(False)
           # self.mRight.ui.pushButton.setDisabled(True)


            wait = WaitWidget()
            #wait.showFullScreen()
            wait.mouseReleaseEvent = self.onClickedEnd

            self.setCentralWidget(wait)
        
        elif self.questionnairecount == self.questionnaire_countdown[0]:
            self.questionnaire_countdown.pop(0)
            self.show_questionnaire()

     
        self.mLeft.banditClickedReceiver.custom_signal.emit()
        self.mRight.banditClickedReceiver.custom_signal.emit()
