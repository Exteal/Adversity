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

        self.left = BanditWidget(leftArm["rewards"], leftArm["a priori"])
        self.left.banditClickedEmitter.custom_signal.connect(lambda: self.onclicked())


        self.right = BanditWidget(rightArm["rewards"], rightArm["a priori"])

        self.right.banditClickedEmitter.custom_signal.connect(lambda: self.onclicked())


        score = self.left.score + self.right.score
        self.scoreWidget = QTextEdit(self)
        self.scoreWidget.setReadOnly(True)
        self.scoreWidget.setText("Score : " + str(score))


        center_layout = QHBoxLayout()
        
        center_layout.addWidget(self.left)
        center_layout.addWidget(self.scoreWidget)
        center_layout.addWidget(self.right)

        main_layout.addLayout(center_layout)
        central_widget.setLayout(main_layout)


    def onclicked(self):
        score = self.left.score + self.right.score
        self.scoreWidget.setText("Score : " + str(score))

        self.left.banditClickedReceiver.custom_signal.emit()
        self.right.banditClickedReceiver.custom_signal.emit()

