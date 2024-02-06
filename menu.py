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
        # Create a tar archive
        tar_menu.addAction('tar -cf', lambda: interface.print_to_terminal('tar -cf archive.tar file1 file2 ... fileN'))
        # Create a tar gzipp'd archive
        tar_menu.addAction('tar -zcf', lambda: interface.print_to_terminal('tar -zcf archive.tar.gz file1 file2 ... fileN'))
        # Create multi-part tar archives from a directory
        tar_menu.addAction('tar cf', lambda: interface.print_to_terminal('tar cf - /path/to/directory|split -b<max_size_of_part>M - archive.tar'))
        # Extract all files from archive
        tar_menu.addAction('tar -xf', lambda: interface.print_to_terminal('tar -xf archive.tar'))
        # Extract from a gzipped archive
        tar_menu.addAction('tar -zxf', lambda: interface.print_to_terminal('tar -zxf archive.tar.gz'))
        # Extract one file from archive
        tar_menu.addAction('tar -xf', lambda: interface.print_to_terminal('tar -xf archive.tar the_one_file'))
        # List files in archive
        tar_menu.addAction('tar -tf', lambda: interface.print_to_terminal('tar -tf archive.tar'))
        # Unzip to target directory
        tar_menu.addAction('-xvf', lambda: interface.print_to_terminal('tar -xvf file.zip -C target_directory_path'))
        
        # Ajouter le sous-menu "tar" au menu principal "Commands"
        commands_menu.addMenu(tar_menu)

        # Créer le sous-menu "grep"
        grep_menu = QMenu('grep', interface)
        # Search for a pattern in a file
        grep_menu.addAction('grep -e', lambda: interface.print_to_terminal('grep -e "pattern" file'))
        grep_menu.addAction('grep -E', lambda: interface.print_to_terminal('grep -E "pattern1|pattern2" file'))
        grep_menu.addAction('grep -v', lambda: interface.print_to_terminal('grep -v "pattern" file'))
        grep_menu.addAction('grep -r', lambda: interface.print_to_terminal('grep -r "pattern" directory'))
        grep_menu.addAction('grep -n', lambda: interface.print_to_terminal('grep -n "pattern" file'))
        grep_menu.addAction('grep -c', lambda: interface.print_to_terminal('grep -c "pattern" file'))
        grep_menu.addAction('grep -l', lambda: interface.print_to_terminal('grep -l "pattern" file'))
        grep_menu.addAction('grep -w', lambda: interface.print_to_terminal('grep -w "pattern" file'))
        grep_menu.addAction('grep -x', lambda: interface.print_to_terminal('grep -x "pattern" file'))
        
        # Ajouter le sous-menu "grep" au menu principal "Commands"
        commands_menu.addMenu(grep_menu)

        # Créer le sous-menu "cp"
        cp_menu = QMenu('cp', interface)
        # Copy files
        cp_menu.addAction('cp', lambda: interface.print_to_terminal('cp source_file destination'))
        # Copy directories recursive
        cp_menu.addAction('cp -R', lambda: interface.print_to_terminal('cp -R source_directory destination'))
        # copy all file but skip existing files (do not overwrite)
        cp_menu.addAction('cp -vrn', lambda: interface.print_to_terminal('cp -vrn source_file destination'))
        # Ajouter le sous-menu "cp" au menu principal "Commands"
        commands_menu.addMenu(cp_menu)

        # Créer le sous-menu "find"
        find_menu = QMenu('find', interface)
        # Find files by name
        find_menu.addAction('find . -name', lambda: interface.print_to_terminal('find <emplacement> -name "<nom fichier>"'))
        # Find files by approximate name
        find_menu.addAction('find . -iname', lambda: interface.print_to_terminal('find <emplacement> -iname "<nom fichier>"'))
        # Find files by type
        find_menu.addAction('find . -type', lambda: interface.print_to_terminal('find <emplacement> -type "f|d" (fichier|dossier)'))
        # Find files by size
        find_menu.addAction('find . -size', lambda: interface.print_to_terminal('find <emplacement> -size +1M'))
        # Find files by date
        find_menu.addAction('find . -mtime', lambda: interface.print_to_terminal('find <emplacement> -mtime +1'))
        # Find files by permissions
        find_menu.addAction('find . -perm', lambda: interface.print_to_terminal('find <emplacement> -perm 777'))
        # Find files by owner
        find_menu.addAction('find . -user', lambda: interface.print_to_terminal('find <emplacement> -user "<nom utilisateur>"'))
        
        # Ajouter le sous-menu "find" au menu principal "Commands"
        commands_menu.addMenu(find_menu)
        
        