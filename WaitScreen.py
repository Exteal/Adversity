from PyQt5.QtWidgets import QMainWindow

class WaitingScreen(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def onClick(self, event):
        self.stack.setCurrentIndex(self.stack.currentIndex() + 1)


        
