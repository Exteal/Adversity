from interface import interface_init
from parameters import ParametersWindow, Types
import sys
from PyQt5.QtWidgets import *
from recommandation import RecommandationWidget
from interfaceBandit2 import InterfaceBandit
import json

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

def load_pages(parameters, interface, stack):
    tuples = parameters.return_types_and_contents()
    
    for typ, content in tuples:
        if typ == Types.RECOMMANDATION:
 
            interface.load_recommandations(RecommandationWidget(content))
            interface.start_interface()

            #interface.interfaceFinishedEmitter.custom_signal.connect(lambda : stack.setCurrentIndex(stack.currentIndex() + 1))

            stack.addWidget(interface)
            stack.update()

        if typ == Types.BANDIT:
            bandito = InterfaceBandit(content["bras"])
            bandito.banditFinishedEmitter.custom_signal.connect(lambda : nextStack(stack))
            stack.addWidget(bandito)
            stack.update()


    stack.setCurrentIndex(stack.currentIndex() + 1) 




def main():
    app = QApplication(sys.argv)
   
    recommandations_path = None
    while recommandations_path == None:
        recommandations_path = choose_directory()
    

    parameters = ParametersWindow(recommandations_path)
    interface = interface_init()
    stack = QStackedWidget()


    parameters.parameters_selected_emitter.custom_signal.connect(lambda : load_pages(parameters, interface, stack))
    
    stack.addWidget(parameters)

    main_layout = QVBoxLayout()
    main_layout.addWidget(stack)


    stack.setCurrentIndex(0)
    stack.showMaximized()


    sys.exit(app.exec())



def testBandit():
    app = QApplication(sys.argv)
   
    params = 0#

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
#testBandit()