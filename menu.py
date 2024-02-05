from PyQt6.QtWidgets import QMenu

# Créer la barre de menu
class Menu:
    
    def __init__(self,interface):
        
        self.interface = interface
        self.menu_bar = interface.menuBar()
        
        # Créer le menu "Commands"
        commands_menu = self.menu_bar.addMenu('Commands')

        # Créer le sous-menu "tar"
        tar_menu = QMenu('tar', interface)
        tar_menu.addAction('Create archive', self.create_tar_archive)
        tar_menu.addAction('Create gzipp\'d archive', self.create_tar_gzipped_archive)
        tar_menu.addAction('Create multi-part archives', self.create_multi_part_tar_archives)
        tar_menu.addAction('Extract all files', self.extract_all_files)
        tar_menu.addAction('Extract all files from gzipped archive', self.extract_from_gzipped_archive)
        tar_menu.addAction('Extract one file', self.extract_one_file)
        tar_menu.addAction('List files in archive', self.list_files_in_archive)

        # Ajouter le sous-menu "tar" au menu principal "Commands"
        commands_menu.addMenu(tar_menu)

        # Créer le sous-menu "grep"
        grep_menu = QMenu('grep', interface)
        grep_menu.addAction('Example Option 1', self.grep_example_option1)
        grep_menu.addAction('Example Option 2', self.grep_example_option2)

        # Ajouter le sous-menu "grep" au menu principal "Commands"
        commands_menu.addMenu(grep_menu)

        # Créer le sous-menu "cp"
        cp_menu = QMenu('cp', interface)
        cp_menu.addAction('Example Option A', self.cp_example_optionA)
        cp_menu.addAction('Example Option B', self.cp_example_optionB)

        # Ajouter le sous-menu "cp" au menu principal "Commands"
        commands_menu.addMenu(cp_menu)
        
        
    
        
    def create_tar_archive(self):
        print("create_tar_archive called")
        self.interface.print_to_terminal('tar -cf archive.tar file1 file2 ... fileN')

    def create_tar_gzipped_archive(self):
        self.interface.print_to_terminal('tar -zcf archive.tar.gz file1 file2 ... fileN')

    def create_multi_part_tar_archives(self):
        self.interface.print_to_terminal('tar cf - /path/to/directory|split -b<max_size_of_part>M - archive.tar')

    def extract_all_files(self):
        self.interface.print_to_terminal('tar -xf archive.tar')

    def extract_from_gzipped_archive(self):
        self.interface.print_to_terminal('tar -zxf archive.tar.gz')

    def extract_one_file(self):
        self.interface.print_to_terminal('tar -xf archive.tar the_one_file')

    def list_files_in_archive(self):
        self.interface.print_to_terminal('tar -tf archive.tar')

    def grep_example_option1(self):
        self.interface.print_to_terminal('grep -e "pattern" file')

    def grep_example_option2(self):
        self.interface.print_to_terminal('grep -E "pattern1|pattern2" file')

    def cp_example_optionA(self):
        self.interface.print_to_terminal('cp source_file destination')

    def cp_example_optionB(self):
        self.interface.print_to_terminal('cp -r source_directory destination')

    