import json
from PyQt5.QtWidgets import QMenu

class Menu:
    def __init__(self, interface):
        self.interface = interface
        self.menu_bar = interface.menuBar()

        # Charger les données JSON depuis le fichier
        with open('commands.json', 'r') as json_file:
            data = json.load(json_file)

        # Créer le menu principal "Commands"
        commands_menu = self.menu_bar.addMenu('Commands')

        # Parcourir les commandes dans le fichier JSON
        for command_data in data:
            command_name = command_data['commande']
            command_description = command_data['description']

            # Créer le sous-menu pour chaque commande
            command_menu = QMenu(command_name, interface)
            command_menu.setTitle(command_description)
            # Ajouter une action pour chaque option de la commande
            for option_data in command_data['options']:
                option = option_data["option"]
                option_description = option_data['description']
                option_exemple = option_data['exemple']
                # Ajouter une action pour chaque option
                action = command_menu.addAction(option_description)
                # Connecter l'action à une fonction
                action.triggered.connect(lambda _, opt=option, cmd=command_name, ex=option_exemple: interface.command_selected(ex, cmd, opt))
                action.hovered.connect(lambda opt=option, cmd=command_name: interface.command_hovered(cmd, opt))
            # Ajouter le sous-menu au menu principal
            commands_menu.addMenu(command_menu)