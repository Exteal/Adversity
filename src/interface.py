from PyQt5.QtGui import QKeyEvent, QMouseEvent, QCursor
from PyQt5.QtWidgets import QLabel, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QSpacerItem, QSizePolicy, QDialog, QFileDialog, QPushButton
from PyQt5.QtCore import QTimer, Qt, pyqtSignal, QObject

from menu import Menu
from terminal import Terminal
from questionnaire import QuestionnaireWidget
from time import perf_counter as pc
from Utils import log_directory
from Styles import recommandationTitleStyle
import csv

class interfaceFinishedEmitter(QObject):
    custom_signal = pyqtSignal()

class InterfaceRecommandation(QMainWindow):
    def __init__(self, log_file, log_quest):
        super().__init__()
        writer = csv.DictWriter(log_file, fieldnames=["time",  "cursor_x", "cursor_y", "event", "widget","terminal_directory", "terminal_input"])
        writer.writeheader()
        self.triggering_widget = None
        self.triggering_event = None
        self.log_file = log_file
        self.log_quest = log_quest


    def load_recommandations(self, recommandation_widget):
        self.recommandation_widget = recommandation_widget


    def start_interface(self):
        self.initUI()
        self.started = pc()

        #self.start_timeout_log()


    def start_timeout_log(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timout_log)
        self.timer.start(2000)
    
    def initUI(self):
        # Créer le widget principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.setMouseTracking(True)
        central_widget.setMouseTracking(True)
        # Créer un layout horizontal pour le widget principal
        main_layout = QHBoxLayout()
        # Créer un layout vertical pour le centre de l'interface
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        # Créer un widget QTextEdit pour l'instruction donnée
        instruction_text = QTextEdit(self)
        instruction_text.setReadOnly(True)
        instruction_text.setText("Sélectionnez une option dans le menu déroulant")

        left_layout.addWidget(instruction_text)
        
        
        self.term = Terminal()
        left_layout.addWidget(self.term)
        
        
        # Ajouter un bouton pour afficher le questionnaire
        questionnaire_button = QPushButton("Répondre au questionnaire")
        questionnaire_button.clicked.connect(self.showQuestionnaire)
        left_layout.addWidget(questionnaire_button)
        
        
        # Créer un layout horizontal pour le côté droit de l'interface
        

        # Créer un layout pour le fil de recommandations
      #  recommendations_list = QVBoxLayout()
    
      
     #   recommendations_list.addWidget(self.recommandation_widget)

   #     spacing = QVBoxLayout()
    #    spacing.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding))
        
        #recommendations_list.addSpacerItem(QSpacerItem(50, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        
        #right_layout.addLayout(recommendations_list, 1)
        right_layout.addSpacerItem(QSpacerItem(200, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        label = QLabel("Cliquez sur la recommandation pour afficher son contenu")
        label.setStyleSheet(recommandationTitleStyle)
        right_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(self.recommandation_widget)
        right_layout.addSpacerItem(QSpacerItem(200, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
       # right_layout.addLayout(spacing, 1)
        

        # Ajouter les layouts
    
        #main_layout.addLayout(left_layout, 33)
        main_layout.addLayout(left_layout, 50)
        main_layout.addLayout(right_layout, 50)

        # Créer le widget central avec le layout principal
        central_widget.setLayout(main_layout)

        # Configuration initiale
        self.setWindowTitle('Interface Example')
        # prend toute la taille de l'écran
        #self.showMaximized()
        
        
         # Créer la barre de menu
        self.menu = Menu(self)
        
    def print_to_terminal(self, text):
        self.term.cursorEnd()
        self.term.cmdWindow.insertPlainText(text)
        
    def command_selected(self, exemple, command_name, option_name):
        # Print et log la commande sélectionnée
        self.print_to_terminal(exemple)
        self.prepare_log("Selected: " + command_name + " " + option_name, "Menu")

    def command_hovered(self, command_name, option_name):
        # log la commande survolée
        self.prepare_log("Hovered: " + command_name + " " + option_name, "Menu")
        
    def log(self):
        mouse_pos = QCursor.pos()
        x, y = mouse_pos.x(), mouse_pos.y()

        writer = csv.DictWriter(self.log_file, fieldnames=[ "time",  "cursor_x", "cursor_y", "event", "widget", "terminal_directory", "terminal_input"])

        writer.writerow({
            "time" : pc() - self.started,
            "cursor_x" : x,
            "cursor_y" : y,
            "event" : self.triggering_event,
            "widget" : self.triggering_widget,
            "terminal_directory" : self.term.get_directory(),
            "terminal_input" : self.term.get_input()
        })
        self.log_file.flush()

    def timout_log(self):
        self.prepare_log("timeout", "")

    def keyPressEvent(self, event):
        self.prepare_log("Key press: " + event.text(), "")
    
    def keyReleaseEvent(self, event):
        self.prepare_log("Key release: " + event.text(), "")

    def mousePressEvent(self, event):
        button = "left" if event.button() == Qt.LeftButton else "right"
        self.prepare_log("Mouse press: " + button, "")
        
    def mouseReleaseEvent(self, event):
        button = "left" if event.button() == Qt.LeftButton else "right"
        self.prepare_log("Mouse release: " + button, "")
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.NoButton:
            self.prepare_log("Mouse move", "")
        else:
            button = "left" if event.buttons() == Qt.LeftButton else "right"
            self.prepare_log("Mouse drag: " + button, "")


    def prepare_log(self, event, widget):
        self.triggering_event = event
        self.triggering_widget = widget
        self.log()
        self.triggering_event = ""
        self.triggering_widget = ""


    def showQuestionnaire(self):
        # Créer une boîte de dialogue modale pour afficher le questionnaire
        dialog = QDialog(self)
        dialog.setWindowTitle("Questionnaire")
        dialog.setModal(True)

        # Créer le widget du questionnaire et ajouter à la boîte de dialogue
        questionnaire_widget = QuestionnaireWidget(self.log_quest)
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(questionnaire_widget)
        dialog.setLayout(dialog_layout)

        # Afficher la boîte de dialogue modale
        dialog.exec_()
        
    def on_close_interface(self):
        self.log_file.close()
        
def interface_init(block_name):
    file =  open(log_directory + "log_recommandations_" + block_name +".csv", "w", newline='')
    quest =  open(log_directory + "log_questionnaire_" + block_name +".csv", "w", newline='')

    interface = InterfaceRecommandation(file, quest)    
    return interface
    