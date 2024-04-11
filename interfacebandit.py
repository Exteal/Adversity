from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QTextEdit

from bandit import BanditWidget


class InterfaceBandit(QMainWindow):
    def __init__(self, bras):
        super().__init__()

        if bras[0]["side"] == "gauche":
            self.initUi(bras[0], bras[1])
        
        else :
            self.initUi(bras[1], bras[0])
        
    
    def initUi(self, leftArm, rightArm):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()

        left = BanditWidget(leftArm["rewards"], leftArm["a priori"])
        left.banditClickedEmitter.custom_signal.connect(lambda: self.onclicked(left, right, scoreWidget))


        right = BanditWidget(rightArm["rewards"], rightArm["a priori"])

        right.banditClickedEmitter.custom_signal.connect(lambda: self.onclicked(left, right, scoreWidget))


        score = left.score + right.score
        scoreWidget = QTextEdit(self)
        scoreWidget.setReadOnly(True)
        scoreWidget.setText("Score : " + str(score))


        center_layout = QHBoxLayout()
        
        center_layout.addWidget(left)
        center_layout.addWidget(scoreWidget)
        center_layout.addWidget(right)

        main_layout.addLayout(center_layout)
        central_widget.setLayout(main_layout)


    def onclicked(self, left, right, scoreWidget):
        score = left.score + right.score
        scoreWidget.setText("Score : " + str(score))

        left.banditClickedReceiver.custom_signal.emit()
        right.banditClickedReceiver.custom_signal.emit()

