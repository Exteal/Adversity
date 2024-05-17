from EndPageWidget import EndPageWidget
from interface import interface_init
from parameters import ParametersWindow, Types
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFontDatabase
from recommandation import RecommandationWidget
from interfacebandit import InterfaceBandit

from Utils import log_directory, user_files_directory
from os import makedirs, path



def choose_directory():

    if user_files_directory:
        return user_files_directory
    
    dial = QFileDialog(caption="Sélectionnez le dossier contenant les fichiers utilisateurs .json")
    dial.setFileMode(QFileDialog.Directory)
    dial.setAcceptMode(QFileDialog.AcceptOpen)
    recom_path = None
    if dial.exec_():
        recom_path = dial.selectedFiles()



    return recom_path[0] if recom_path else None




def nextStack(stack):
    stack.setCurrentIndex(stack.currentIndex() + 1)

def load_pages(block_infos, stack, parameters):
    for block in reversed(block_infos):
        if block["type"] == Types.RECOMMANDATION:

            interface = interface_init(block["name"])

            recoms = RecommandationWidget(block["content"])
            
            interface.load_recommandations(recoms)
            interface.start_interface()

            recoms.nextPage.custom_signal.connect(lambda :nextStack(stack))

            stack.insertWidget(1, interface)
            stack.update()

        if block["type"] == Types.BANDIT:
            bandito = InterfaceBandit(block["content"]["bras"], block["name"], block["content"]["chargements_questionnaire"])
            bandito.nextPage.custom_signal.connect(lambda : nextStack(stack))
            stack.insertWidget(1, bandito)
            stack.update()
        
    stack.addWidget(EndPageWidget(stack))
    nextStack(stack)




def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Choix du participant")

    makedirs(path.dirname(log_directory), exist_ok=True)
    recommandations_path = choose_directory()
    
    if recommandations_path == None:
        sys.exit()

    

    parameters = ParametersWindow(recommandations_path)
    stack = QStackedWidget()


    parameters.parameters_selected_emitter.custom_signal.connect(lambda block_infos: load_pages(block_infos, stack, parameters))
    
    stack.addWidget(parameters)

    main_layout = QVBoxLayout()
    main_layout.addWidget(stack)


    stack.setCurrentIndex(0)
    stack.showMaximized()

        
    # fonts = QFontDatabase()
    # names = fonts.families()
    # print(names)
    sys.exit(app.exec())


main()
