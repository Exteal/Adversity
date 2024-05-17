from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSlider, QLabel, QPushButton, QApplication
from DoubleSlider import QRangeSlider

import csv

class QuestionnaireWidget(QWidget):
    def __init__(self, log_quest):
        super().__init__()
        self.log_quest = log_quest
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout()

        # Question 1: Précision de la recommandation
        label1 = QLabel("1) À combien estimes-tu le niveau de précision de la recommandation?")

        
        self.slider1 = QRangeSlider()
        self.slider1.setRange(0, 10)  # Valeurs entre 0 et 100
      #  self.slider1.setTickInterval(1)  # Intervalles de 10 %
      #  self.slider1.setTickPosition(QSlider.TicksBelow)  # Affichage des graduations sous le slider
      #  self.slider1.setSingleStep(1)  
        label1_value = QLabel(str(self.slider1.start())+" à " + str(self.slider1.end())+ " %")

        # Question 2: Temps gagné lorsque le système est correct
        label2 = QLabel("2) Quand le système est correct, combien de temps te fait-il gagner?")
        self.slider2 = QRangeSlider()
        self.slider2.setRange(0, 2) 
        self.slider2.setMax(5) # Valeurs entre 0 et 100
        # self.slider2.setTickInterval(1)  # Intervalles de 1 minute
        # self.slider2.setTickPosition(QSlider.TicksBelow)  # Affichage des graduations sous le slider
        # self.slider2.setSingleStep(1)  
        label2_value = QLabel(str(self.slider2.start())+" à " + str(self.slider2.end())+ " minutes")

        # Question 3: Temps perdu lorsque le système est incorrect
        label3 = QLabel("3) Quand le système est incorrect, il te fait perdre combien de temps?")
        self.slider3 = QRangeSlider()
        self.slider3.setRange(0, 2)  # Valeurs entre 0 et 100
        self.slider3.setMax(5)

        # self.slider3.setTickInterval(1)  # Intervalles de 1 minute
        # self.slider3.setTickPosition(QSlider.TicksBelow)  # Affichage des graduations sous le slider
        # self.slider3.setSingleStep(1)  
        label3_value = QLabel(str(self.slider3.start())+" à " + str(self.slider3.end())+ " minutes")
        
        #self.setSliderInterval(self.slider1, 5)
        #self.setSliderInterval(self.slider2, 60)  # Pour les minutes
        #self.setSliderInterval(self.slider3, 60)  # Pour les minutes

        # Connecter les sliders aux labels de valeurs

     
        self.slider1.startValueChanged.connect(lambda value: label1_value.setText(str(value)+" à " + str(self.slider1.end())+ " %"))
        self.slider1.endValueChanged.connect(lambda value: label1_value.setText(str(self.slider1.start())+ " à " + str(value) + " %"))
        

        self.slider2.startValueChanged.connect(lambda value: label2_value.setText(str(value)+" à " + str(self.slider2.end())+ " minutes"))
        self.slider2.endValueChanged.connect(lambda value: label2_value.setText(str(self.slider2.start())+ " à " + str(value) + " minutes"))

        self.slider3.startValueChanged.connect(lambda value: label3_value.setText(str(value)+" à " + str(self.slider3.end())+ " minutes"))
        self.slider3.endValueChanged.connect(lambda value: label3_value.setText(str(self.slider3.start())+ " à " + str(value) + " minutes"))

        # self.slider2.valueChanged.connect(lambda value: label2_value.setText(str(value*10)+" secondes"))
        
        # self.slider3.valueChanged.connect(lambda value: label3_value.setText(str(value*10)+" secondes"))

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

        writer = csv.DictWriter(self.log_quest, fieldnames=["precision_min", "precision_max", "temps_gagne_min", "temps_gagne_max", "temps_perdu_min", "temps_perdu_max"])
        writer.writeheader()

        writer.writerow({
            "precision_min" : self.slider1.start(),
            "precision_max" : self.slider1.end(),
            "temps_gagne_min" : self.slider2.start(),
            "temps_gagne_max" :  self.slider2.end(),
            "temps_perdu_min" :  self.slider3.start(),
            "temps_perdu_max" :  self.slider3.end()
        })
        self.log_quest.flush()
        self.parent().close()

        #self.log_quest.close()














class QuestionnaireWidgetBandit(QWidget):
    def __init__(self, log_quest):
        super().__init__()
        self.log_quest = log_quest
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout()

        # Question 1: Précision de la recommandation
        label1 = QLabel("1) À combien estimes-tu le gain moyen du bras gauche ?")

        
        self.slider1 = QRangeSlider()
        self.slider1.setRange(5, 10)  # Valeurs entre 0 et 100
        self.slider1.setMax(100) # Valeurs entre 0 et 100

      #  self.slider1.setTickInterval(1)  # Intervalles de 10 %
      #  self.slider1.setTickPosition(QSlider.TicksBelow)  # Affichage des graduations sous le slider
      #  self.slider1.setSingleStep(1)  
        label1_value = QLabel(str(self.slider1.start())+" à " + str(self.slider1.end()))

        # Question 2: Temps gagné lorsque le système est correct
        label2 = QLabel("2) À combien estimes-tu le gain moyen du bras droit?")
        self.slider2 = QRangeSlider()
        self.slider2.setRange(0, 5) 
        self.slider2.setMax(100) # Valeurs entre 0 et 100
        # self.slider2.setTickInterval(1)  # Intervalles de 1 minute
        # self.slider2.setTickPosition(QSlider.TicksBelow)  # Affichage des graduations sous le slider
        # self.slider2.setSingleStep(1)  
        label2_value = QLabel(str(self.slider2.start())+" à " + str(self.slider2.end()))

        # Question 3: Temps perdu lorsque le système est incorrect
      
        #self.setSliderInterval(self.slider1, 5)
        #self.setSliderInterval(self.slider2, 60)  # Pour les minutes
        #self.setSliderInterval(self.slider3, 60)  # Pour les minutes

        # Connecter les sliders aux labels de valeurs

     
        self.slider1.startValueChanged.connect(lambda value: label1_value.setText(str(value)+" à " + str(self.slider1.end())))
        self.slider1.endValueChanged.connect(lambda value: label1_value.setText(str(self.slider1.start())+ " à " + str(value)))
        

        self.slider2.startValueChanged.connect(lambda value: label2_value.setText(str(value)+" à " + str(self.slider2.end())))
        self.slider2.endValueChanged.connect(lambda value: label2_value.setText(str(self.slider2.start())+ " à " + str(value)))

      
        # self.slider2.valueChanged.connect(lambda value: label2_value.setText(str(value*10)+" secondes"))
        
        # self.slider3.valueChanged.connect(lambda value: label3_value.setText(str(value*10)+" secondes"))

        # Bouton de soumission
        submit_button = QPushButton("Soumettre")


        layout.addWidget(label1)
        layout.addWidget(self.slider1)
        layout.addWidget(label1_value)
        layout.addWidget(label2)
        layout.addWidget(self.slider2)
        layout.addWidget(label2_value)
        layout.addWidget(submit_button)

        self.setLayout(layout)

        submit_button.clicked.connect(self.submitAnswers)
        
    def setSliderInterval(self, slider, interval):
        slider.valueChanged.connect(lambda value: slider.setSliderPosition((value // interval) * interval))

    def submitAnswers(self):

        writer = csv.DictWriter(self.log_quest, fieldnames=["gain_gauche_min", "gain_gauche_max",  "gain_droit_min", "gain_droit_max"])
        writer.writeheader()

        writer.writerow({
            "gain_gauche_min" : self.slider1.start(),
            "gain_gauche_max" : self.slider1.end(),
            "gain_droit_min" : self.slider2.start(),
            "gain_droit_max" :  self.slider2.end(),
           
        })
        self.log_quest.flush()
        self.parent().close()