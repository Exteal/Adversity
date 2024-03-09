import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtGui import *
from menu import Menu
from recommand_lib import recommand

class Interface(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

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
        self.terminal_output = QPlainTextEdit(self)
        self.terminal_output.setReadOnly(True)
        center_layout.addWidget(self.terminal_output)

        # Créer un widget QLineEdit pour saisir les commandes du terminal
        self.command_input = QLineEdit(self)
        self.command_input.setPlaceholderText("Entrez une commande...")
        self.command_input.returnPressed.connect(self.run_command)
        center_layout.addWidget(self.command_input)
        
        # Créer un processus pour exécuter le terminal
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.update_output)
        
        
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
        left_layout = QVBoxLayout()
        # text pour le titre
        title = QLabel("Recherche Web")
        title.setAlignment(Qt.AlignmentFlag.AlignTop)
        title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        
        # ajouter une case de recherche
        #search_bar = QLineEdit(self)
        #search_bar.setPlaceholderText("Entrez une recherche...")
        # ajouter un bouton de recherche
        #search_button = QPushButton("Rechercher")
        # ajouter les widgets au layout
        #left_layout.addWidget(search_bar)

        web_view = QWebEngineView(self)
        web_view.setUrl(QUrl("https://google.com"))
        web_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        left_layout.addWidget(title)
        left_layout.addWidget(web_view)

        # Ajouter les layouts
    
        main_layout.addLayout(left_layout, 33)
        main_layout.addLayout(center_layout, 33)
        main_layout.addLayout(right_layout, 33)

        # Créer le widget central avec le layout principal
        central_widget.setLayout(main_layout)

        # Configuration initiale
        self.setWindowTitle('Interface Example')
        # prend toute la taille de l'écran
        self.showMaximized()
        
        
         # Créer la barre de menu
        self.menu = Menu(self)
        
    def print_to_terminal(self, text):
        self.command_input.setText(text)
        
    def test_action_triggered(self):
        print("Test action triggered!")

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

def main(args):
    app = QApplication(args)
    interface = Interface()
    interface.show()
    sys.exit(app.exec())
    
    
if __name__ == '__main__':
    main(sys.argv)
    