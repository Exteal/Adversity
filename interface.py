import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from menu import Menu
from recommand_lib import recommand
from terminal import Terminal
from time import perf_counter as pc
import csv

class Interface(QMainWindow):
    def __init__(self, log_file):
        super().__init__()
        self.triggering_widget = None
        self.triggering_event = None
        self.log_file = log_file

        self.initUI()
        self.started = pc()

        self.start_timeout_log()


    def start_timeout_log(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timout_log)
        self.timer.start(2000)
    
    def initUI(self):
        # Créer le widget principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Créer un layout horizontal pour le widget principal
        main_layout = QHBoxLayout()
        # Créer un layout vertical pour le centre de l'interface
        center_layout = QVBoxLayout()

        # Créer un widget QComboBox pour le menu déroulant
        #menu_combobox = QComboBox(self)
        #menu_combobox.addItem("tar")
        #menu_combobox.addItem("grep")
        #menu_combobox.addItem("cp")
        #center_layout.addWidget(menu_combobox)
        
        # Créer un widget QTextEdit pour l'instruction donnée
        instruction_text = QTextEdit(self)
        instruction_text.setReadOnly(True)
        instruction_text.setText("Sélectionnez une option dans le menu déroulant")
        center_layout.addWidget(instruction_text)

        # Créer un widget QPlainTextEdit pour le terminal
        #self.terminal_output = QPlainTextEdit(self)
        #self.terminal_output.setReadOnly(True)
        #center_layout.addWidget(self.terminal_output)

        # Créer un widget QLineEdit pour saisir les commandes du terminal
        #self.command_input = QLineEdit(self)
        #self.command_input.setPlaceholderText("Entrez une commande...")
        #self.command_input.returnPressed.connect(self.run_command)
        #center_layout.addWidget(self.command_input)
        
        self.term = Terminal()
        center_layout.addWidget(self.term)
        
        # Créer un processus pour exécuter le terminal
        #self.process = QProcess(self)
        #self.process.readyReadStandardOutput.connect(self.update_output)
        
        
        # Créer un layout horizontal pour le côté droit de l'interface
        right_layout = QVBoxLayout()

        # Créer un layout pour le fil de recommandations
        recommendations_list = QVBoxLayout()
    
        for item in recommand():
            recommendations_list.addWidget(item)

        spacing = QVBoxLayout()
        spacing.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding))
        
        #recommendations_list.addSpacerItem(QSpacerItem(50, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        
        right_layout.addLayout(recommendations_list, 1)
        right_layout.addLayout(spacing, 1)
        
        # Créer un widget QWebView pour l'accès au web
        #left_layout = QVBoxLayout()
        # text pour le titre
        #title = QLabel("Recherche Web")
        #title.setAlignment(Qt.AlignmentFlag.AlignTop)
        #title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        
        # ajouter une case de recherche
        #search_bar = QLineEdit(self)
        #search_bar.setPlaceholderText("Entrez une recherche...")
        # ajouter un bouton de recherche
        #search_button = QPushButton("Rechercher")
        # ajouter les widgets au layout
        #left_layout.addWidget(search_bar)

        #web_view = QWebEngineView(self)
        #web_view.setUrl(QUrl("https://google.com"))
        #web_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        #left_layout.addWidget(title)
        #left_layout.addWidget(web_view)

        # Ajouter les layouts
    
        #main_layout.addLayout(left_layout, 33)
        main_layout.addLayout(center_layout)
        main_layout.addLayout(right_layout)

        # Créer le widget central avec le layout principal
        central_widget.setLayout(main_layout)

        # Configuration initiale
        self.setWindowTitle('Interface Example')
        # prend toute la taille de l'écran
        self.showMaximized()
        
        
         # Créer la barre de menu
        self.menu = Menu(self)
        
    def print_to_terminal(self, text):
        self.term.cmdWindow.insertPlainText(text)
        

    def run_command(self):
        # Récupérer la commande saisie par l'utilisateur
        command = self.command_input.text()

        # Exécuter la commande dans le processus
        self.process.start(command)
        self.process.waitForFinished()

    def update_output(self):
        # Mettre à jour la sortie du terminal à partir du processus
        output = self.process.readAllStandardOutput().data().decode('utf-8')
        self.terminal_output.appendPlainText(output)

    def clear_terminal(self):
        # Effacer la sortie du terminal
        self.terminal_output.clear()


    def log(self):
        mouse_pos = QCursor.pos()
        x, y = mouse_pos.x(), mouse_pos.y()

        writer = csv.DictWriter(self.log_file, fieldnames=["event", "widget", "cursor", "timing"])

        writer.writerow({
            "event" : self.triggering_event,
            "widget" : self.triggering_widget,
            "cursor" : f"({x},{y})",
            "timing" : pc() - self.started
        })
        self.log_file.flush()

    def timout_log(self):
        self.prepare_log("timeout", "")

    def keyPressEvent(self, event):
        self.prepare_log("Key press " + event.text(), "")

    def mousePressEvent(self, event):
        button = "left" if event.button() == Qt.LeftButton else "right"
        self.prepare_log("Mouse press " + button, "")


    def prepare_log(self, event, widget):
        self.triggering_event = event
        self.triggering_widget = widget
        self.log()
        self.triggering_event = ""
        self.triggering_widget = ""


def main(args):
    app = QApplication(args)
    with open("log.csv", "w", newline='') as file:
        interface = Interface(file)
        interface.show()
        sys.exit(app.exec())
    
    
if __name__ == '__main__':
    main(sys.argv)
    