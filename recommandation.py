from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtGui import * 

from PyQt6.QtCore import Qt

class Recommandation():
    def __init__(self, header, body):
        self.header = header
        self.body = body


class RecommandationWidget(QWidget):
    def __init__(self, header, body, timeout):
        QWidget.__init__(self)
        self.recommandation = Recommandation(header, body)
        self.revealed = False
        self.content = self.recommandation.header
        self.timeout = timeout
        self.timer = None


    def mousePressEvent(self, event):
        if self.timer == None:
            self.timer = QTimer(self)
            self.timer.setSingleShot(True)
            self.timer.timeout.connect(self.reveal)
            self.timer.start(self.timeout)

       
    
    def reveal(self):
        if self.revealed:
            self.content = self.recommandation.header
        else:  
            self.content = self.recommandation.body
        self.revealed = not(self.revealed)
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


        painter.fillRect(QRect(0,0, width, height), QColor("red"))
        painter.drawText(QPoint(int(width/3), int(height/2)), self.content)
        
        #painter.drawLine(0,0, width, 0)
        #painter.drawLine(0,height, width, height)

        #painter.drawLine(0,0, 0, height)
        #painter.drawLine(width, 0, width, height)


        #self.setFrameStyle(QFrame.Panel)
