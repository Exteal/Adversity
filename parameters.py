from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import * 
import json
import os
import glob
from recommandation import Recommandation




class ParametersSelectedEmitter(QObject):
    custom_signal = pyqtSignal(list)


class ParametersWindow(QMainWindow):
    def __init__(self, recommandations_directory_path):
        QWidget.__init__(self)


        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Créer un layout horizontal pour le widget principal
        main_layout = QHBoxLayout()


        #directory_path = self.choose_directory()
        self.json_data = self.find_participants_json(recommandations_directory_path)
        
        self.names_widget = self.create_names_widget()
        self.blocks_widget = QListWidget()
        self.names_widget.itemSelectionChanged.connect(lambda: self.change_block_items())

        self.blocks_widget.itemSelectionChanged.connect(lambda:  self.emi())
                                                        #self.return_recommandations())
        #self.names_widget.show()
        #self.blocks_widget.show()



        main_layout.addWidget(self.names_widget)
        main_layout.addWidget(self.blocks_widget)

        central_widget.setLayout(main_layout)

        # Configuration initiale
        self.setWindowTitle('Experiment parameters')

        self.parameters_selected_emitter = ParametersSelectedEmitter()
        # prend toute la taille de l'écran
        #self.showMaximized()
    
    
    def emi(self):
        recoms = self.return_recommandations()
        self.parameters_selected_emitter.custom_signal.emit(recoms)


    def change_block_items(self):
        name_selected = self.names_widget.currentItem().text()

        self.blocks_widget.clear()
        for data in self.json_data:
            if data["participant"] == name_selected:
                blocks = data["blocks"]
                for block in blocks:
                    block_name = block["block_name"]
                    QListWidgetItem(block_name, self.blocks_widget)


    def return_recommandations(self):
        name_selected = self.names_widget.currentItem().text()
        block_selected = self.blocks_widget.currentItem().text()


        for data in self.json_data:
            if data["participant"] == name_selected:
                blocks = data["blocks"]
                for block in blocks:
                    if block["block_name"] == block_selected:
                        content = block["block_content"]
                        recommandation_list = self.create_recommandation_list(content)
                        return recommandation_list


    def create_recommandation_list(self, content):
        recoms = []
        for recommandation in content:
            recoms.append(Recommandation(recommandation["header"], recommandation["body"], recommandation["timeout_seconds"] * 1000))
        return recoms


    def create_names_widget(self):
        names = self.list_participants_names()

        names_widget = QListWidget()
        for name in names:
            QListWidgetItem(name, names_widget)
        return names_widget




   
    
    def find_participants_json(self, path):
        json_files = glob.glob(os.path.join(path[0], '*.json'))
        
        json_data = []
        for file in json_files :
           with open(file) as f:
            dataframe = json.load(f)
            if self.is_participant_file_format(dataframe):
                json_data.append(dataframe)
        return json_data

    def is_participant_file_format(self, dataframe):
        return type(dataframe) == dict and set(dataframe.keys()) == set(["participant", "blocks"])
    

    def list_participants_names(self):
        names = []

        for data in self.json_data:
            name = data["participant"]
            names.append(name)
        return names