from EndPageWidget import EndPageWidget
from interface import interface_init
from parameters import ParametersWindow, Types
import sys
from PyQt5.QtWidgets import *
from recommandation import RecommandationWidget
from interfaceBandit2 import InterfaceBandit
import json
from WaitScreen import WaitingScreen



def choose_directory():
    dial = QFileDialog()
    dial.setFileMode(QFileDialog.Directory)
    dial.setAcceptMode(QFileDialog.AcceptOpen)
    path = None
    if dial.exec_():
        path = dial.selectedFiles()
    return path




def nextStack(stack):
    stack.setCurrentIndex(stack.currentIndex() + 1)

def load_pages(block_infos, stack):
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
            bandito = InterfaceBandit(block["content"]["bras"])
            bandito.nextPage.custom_signal.connect(lambda : nextStack(stack))
            stack.insertWidget(1, bandito)
           # stack.addWidget(WaitingScreen())
            stack.update()


    stack.addWidget(EndPageWidget(stack))
    stack.setCurrentIndex(stack.currentIndex() + 1) 




def main():
    app = QApplication(sys.argv)
   
    recommandations_path = None
    while recommandations_path == None:
        recommandations_path = choose_directory()
    

    parameters = ParametersWindow(recommandations_path)
    stack = QStackedWidget()


    parameters.parameters_selected_emitter.custom_signal.connect(lambda block_infos: load_pages(block_infos, stack))
    
    stack.addWidget(parameters)

    main_layout = QVBoxLayout()
    main_layout.addWidget(stack)


    stack.setCurrentIndex(0)
    stack.showMaximized()


    sys.exit(app.exec())



def testBandit():
    app = QApplication(sys.argv)
   
    params = 0

    with open("recommandations/recommandation_bandit.json", "r") as file :
        js = json.load(file)
    
    blocks = js["blocks"]

    params = []
    for block in blocks:
        if block["block_type"] == "bandit":
            params.append(block["block_content"]["bras"])


    bandito = InterfaceBandit(params[0])
    bandito.show()

    sys.exit(app.exec())

main()
