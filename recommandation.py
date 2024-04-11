from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import * 

from PyQt5.QtCore import Qt

class Recommandation():
    def __init__(self, header, body, timeout):
        self.header = header
        self.body = body
        self.timeout = timeout
    def __repr__(self) -> str:
        return str(self.header) + " : " + str(self.body)




class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    
    def __init__(self, maximum):
        QObject.__init__(self)
        self.value = 0
        self.maximum = maximum

    def run(self):
        self.time = QTimer(self)

        if self.maximum == 0:
            self.finished.emit()
        else :
            self.time.timeout.connect(self.incr)
            self.time.start(1000)
       
    def incr(self):
        self.value = self.value + 1
        if self.value == self.maximum:
            self.finished.emit()
            self.time.stop()
        else:
            self.progress.emit(self.value)



class RecommandationWidget(QWidget):
    def __init__(self, recommandation_list):
        super().__init__(self)
        self.recommandation_list = recommandation_list
        self.recommandation = self.recommandation_list.pop(0)
        self.revealed = False
        self.content = self.recommandation.header
        self.timer = None
        self.color = QColor("white")
        self.progress = QProgressBar(self)
        self.progress.hide()


    def log_to_interface(self, event, widget=""):
        
        interface = self.parent().parent()
        interface.prepare_log(event, widget)
       


    def mousePressEvent(self, event):
        button = "left" if event.button() == Qt.LeftButton else "right"
        recomm = "Recommandation " + self.recommandation.header
        
        self.log_to_interface("Clicked " + button, recomm)
        

        if self.revealed:
           self.processNextRecommandation()
        
        else :
            if self.timer == None:
                self.timer = QTimer(self)
                self.timer.setSingleShot(True)
                self.timer.timeout.connect(self.reveal)
                self.timer.start(self.recommandation.timeout)
                self.initProgress()
            

    def initProgress(self):
        maximum = self.recommandation.timeout / 1000

        self.progress.setRange(0, maximum)
        self.progress.setValue(0)

        self.progress.show()
        
        self.thread = QThread(self)
        self.worker = Worker(maximum)
        
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        
        
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)

        self.thread.start()
  

   
    def reportProgress(self, value):

        self.progress.setValue(value)
        self.update()
        



    def processNextRecommandation(self) :
        if not self.recommandation_list:
            self.deleteWidget()
            return
        self.progress.hide()
        self.recommandation = self.recommandation_list.pop(0)
        self.content = self.recommandation.header
        self.timer = None
        self.revealed = False
        self.update()

    ### TODO
    def deleteWidget(self):
        self.deleteLater()
    

    def enterEvent(self, event):
        recomm = "Recommandation " + self.recommandation.header
        self.log_to_interface("Started hovering", recomm)

        self.color = QColor("gray")
        self.update()

    def leaveEvent(self, event):
        recomm = "Recommandation " + self.recommandation.header
        self.log_to_interface("Finished hovering", recomm)


        self.color = QColor("white")
        self.update()


    def reveal(self):
        self.content = self.recommandation.body
        self.revealed = True
        self.timer = None
        self.progress.hide()

        self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        
        pen = QPen()
        brush = QBrush()

        #font = QFont("Verdana")
        #font.setPixelSize(12)
        #pen.setStyle(Qt.PenStyle.DashDotLine)
        pen.setWidth(12)
        #painter.setFontSize(12)
       #pen.setBrush(QColor("red"))
        
        brush.setColor(QColor("black"))
        
        #painter.setFont(font)
        #bounds = QRect()
        #painter.drawText(bounds.adjusted(0, 0, -pen.width(), -pen.width()), 0, self.content)
        #painter.end()
        width,height = self.size().width(), self.size().height()


       # painter.setBackgroundMode(Qt.BGMode.OpaqueMode)
        #painter.setBackground(brush)
        
        painter.setPen(pen)
        painter.setBrush(brush)


        painter.fillRect(QRect(0,0, width, height), self.color)
        painter.drawText(QPoint(int(width/3), int(height/2)), self.content)
        
        #painter.drawLine(0,0, width, 0)
        #painter.drawLine(0,height, width, height)

        #painter.drawLine(0,0, 0, height)
        #painter.drawLine(width, 0, width, height)


        #self.setFrameStyle(QFrame.Panel)
