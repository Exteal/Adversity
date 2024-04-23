from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSlider, QLabel, QPushButton, QApplication

class QuestionnaireWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Question 1: Précision de la recommandation
        label1 = QLabel("1) À combien estimes-tu le niveau de précision de la recommandation?")
        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setRange(0, 10)  # Valeurs entre 0 et 100
        self.slider1.setTickInterval(1)  # Intervalles de 10 %
        self.slider1.setTickPosition(QSlider.TicksBelow)  # Affichage des graduations sous le slider
        self.slider1.setSingleStep(1)  
        label1_value = QLabel("")

        # Question 2: Temps gagné lorsque le système est correct
        label2 = QLabel("2) Quand le système est correct, combien de temps te fait-il gagner?")
        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setRange(0, 10)  # Valeurs entre 0 et 100
        self.slider2.setTickInterval(1)  # Intervalles de 1 minute
        self.slider2.setTickPosition(QSlider.TicksBelow)  # Affichage des graduations sous le slider
        self.slider2.setSingleStep(1)  
        label2_value = QLabel("")

        # Question 3: Temps perdu lorsque le système est incorrect
        label3 = QLabel("3) Quand le système est incorrect, il te fait perdre combien de temps?")
        self.slider3 = QSlider(Qt.Horizontal)
        self.slider3.setRange(0, 10)  # Valeurs entre 0 et 100
        self.slider3.setTickInterval(1)  # Intervalles de 1 minute
        self.slider3.setTickPosition(QSlider.TicksBelow)  # Affichage des graduations sous le slider
        self.slider3.setSingleStep(1)  
        label3_value = QLabel("")
        
        #self.setSliderInterval(self.slider1, 5)
        #self.setSliderInterval(self.slider2, 60)  # Pour les minutes
        #self.setSliderInterval(self.slider3, 60)  # Pour les minutes

        # Connecter les sliders aux labels de valeurs
        self.slider1.valueChanged.connect(lambda value: label1_value.setText(str(value*10)+"%"))
        self.slider2.valueChanged.connect(lambda value: label2_value.setText(str(value*10)+" secondes"))
        self.slider3.valueChanged.connect(lambda value: label3_value.setText(str(value*10)+" secondes"))

        # Bouton de soumission
        submit_button = QPushButton("Soumettre")


        layout.addWidget(label1)
        layout.addWidget(self.slider1)
        layout.addWidget(label1_value)
        layout.addWidget(label2)
        layout.addWidget(self.slider2)
        layout.addWidget(label2_value)
        layout.addWidget(label3)
        layout.addWidget(self.slider3)
        layout.addWidget(label3_value)
        layout.addWidget(submit_button)

        self.setLayout(layout)

        submit_button.clicked.connect(self.submitAnswers)
        
    def setSliderInterval(self, slider, interval):
        slider.valueChanged.connect(lambda value: slider.setSliderPosition((value // interval) * interval))

    def submitAnswers(self):
        # TODO: Stocker les réponses dans un fichier
        pass


if __name__ == '__main__':
    app = QApplication([])
    window = QuestionnaireWidget()
    window.show()
    app.exec_()