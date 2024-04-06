from interface import interface_init
from parameters import ParametersWindow
import sys
from PyQt5.QtWidgets import *
from recommandation import RecommandationWidget



def choose_directory():
    dial = QFileDialog()
    dial.setFileMode(QFileDialog.Directory)
    dial.setAcceptMode(QFileDialog.AcceptOpen)
    path = None
    if dial.exec_():
        path = dial.selectedFiles()
    return path


def load_interface(parameters, interface, stack):
    recoms = parameters.return_recommandations()
    
    interface.load_recommandations(RecommandationWidget(recoms))
    interface.start_interface()
    stack.setCurrentIndex(1)

    stack.update()



def main():
    app = QApplication(sys.argv)
   
    recommandations_path = None
    while recommandations_path == None:
        recommandations_path = choose_directory()
    

    parameters = ParametersWindow(recommandations_path)
    interface = interface_init()
    stack = QStackedWidget()

    parameters.parameters_selected_emitter.custom_signal.connect(lambda : load_interface(parameters, interface, stack))

    
    stack.addWidget(parameters)
    stack.addWidget(interface)

    main_layout = QVBoxLayout()
    main_layout.addWidget(stack)


    stack.setCurrentIndex(0)
    stack.showMaximized()


    sys.exit(app.exec())



main()