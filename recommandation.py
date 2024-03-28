from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtGui import * 

from PyQt6.QtCore import Qt

class Recommandation():
    def __init__(self, header, body, timeout):
        self.header = header
        self.body = body
        self.timeout = timeout
    def __repr__(self) -> str:
        return str(self.header) + " : " + str(self.body)




class RecommandationWidget(QWidget):
    def __init__(self, recommandation_list):
    #def __init__(self, header, body, timeout):
        QWidget.__init__(self)
        self.recommandation_list = recommandation_list
        #self.recommandation = Recommandation(header, body)
        self.recommandation = self.recommandation_list.pop(0)
        self.revealed = False
        self.content = self.recommandation.header
        self.timer = None
        self.color = QColor("red")


    def mousePressEvent(self, event):

        interface = self.parent().parent()
        interface.click_zone = "Recommandation : " + self.recommandation.header
        interface.log_data()

        if self.revealed:
           self.processNextRecommandation()
        
        else :
            if self.timer == None:
                self.timer = QTimer(self)
                self.timer.setSingleShot(True)
                self.timer.timeout.connect(self.reveal)
                self.timer.start(self.recommandation.timeout)
            
    def enterEvent(self, event):
        self.color = QColor("blue")
        self.update()

        interface = self.parent().parent()
        interface.recommendation_event = "Enter"
        interface.log_data()
        print("iiiii ", interface.recommendation_event)
        interface.recommendation_event = "None"
        #TODO ajouter log

       
    def leaveEvent(self, event):
        self.color = QColor("red")
        self.update()

        interface = self.parent().parent()
        interface.recommendation_event = "Leave"
        interface.log_data()
        interface.recommendation_event = "None"

        #TODO ajouter log
    


    def processNextRecommandation(self) :
        if not self.recommandation_list:
            self.deleteWidget()
            return
        self.recommandation = self.recommandation_list.pop(0)
        self.content = self.recommandation.header
        self.timer = None
        self.revealed = False
        self.update()

    ### TODO
    def deleteWidget(self):
        self.deleteLater()
    

    def reveal(self):
        self.content = self.recommandation.body
        self.revealed = True
        self.timer = None
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
