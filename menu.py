import json
from PyQt6.QtWidgets import QMenu

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
            for option, option_data in command_data['option'].items():
                option_description = option_data['description']
                option_exemple = option_data['exemple']

                # Ajouter l'action au sous-menu
                command_menu.addAction(option_description, lambda exemple=option_exemple: interface.print_to_terminal(exemple))


            # Ajouter le sous-menu au menu principal
            commands_menu.addMenu(command_menu)
