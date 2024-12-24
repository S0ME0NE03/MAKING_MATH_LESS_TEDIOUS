import importlib
import os
import sys

from file_manager import FileManager
from program_logging import logging
from commands import Commands

class Calculator:
    def __init__(self) -> None:
        #If you change the order of this it can break
        self.set_up_system_variables()

        self.file_manager = FileManager(self)
        self.program_logging = logging(self)

        self.set_up_add_ons()
        self.commands = Commands(self)

        self.welcome_message()
    
    def set_up_system_variables(self):
        self.MAIN_PROGRAM_PATH : str = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.GITHUB_ADD_ONS_URL : str = "https://github.com/S0ME0NE03/MAKING_MATH_LESS_TEDIOUS/tree/Making_Math_Less_Tedious-COMPLETE-version-1.0.0.0/add_ons"
        self.GITHUB_ADD_ONS_URL_RAW : str = "https://raw.githubusercontent.com/S0ME0NE03/MAKING_MATH_LESS_TEDIOUS/refs/heads/main/add_ons"
        self.repo_owner = "S0ME0NE03"  # Replace with the repository owner
        self.repo_name = "MAKING_MATH_LESS_TEDIOUS"  # Replace with your repository name
        self.api_url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/contents/add_ons"

        self.program_running : bool = True
        self.command = None

    def set_up_add_ons(self):
        self.ADD_ONS_PATH : str = os.path.join(self.MAIN_PROGRAM_PATH, "add_ons")
        self.add_ons_filename_list: list[str] = []
        self.add_ons_modules = []

        if not self.file_manager.folder_exits(self.ADD_ONS_PATH):
            self.file_manager.create_folder(folder_name="add_ons", folder_path = self.MAIN_PROGRAM_PATH)
        
        if self.ADD_ONS_PATH not in sys.path:
            sys.path.append(self.ADD_ONS_PATH)

        for filename in os.listdir(self.ADD_ONS_PATH):
            if filename.endswith('.py'):
                module_name = filename[:-3]  # Strip the .py extension
                try:
                    module = importlib.import_module(module_name)
                    if hasattr(module, 'main'):
                        self.append_to_add_on_modules_list(module)
                        self.append_to_add_on_file_name_list(module_name)
                    else:
                        self.program_logging.error_log(f"Module \"{module_name}\" does not have a \"main\" function so it cannot be run by the launcher")
                except ImportError as e:
                    print(f"Error importing {module_name}: {e}")
    
    def append_to_add_on_file_name_list(self, add_on_name: str) -> None:
        self.add_ons_filename_list.append(add_on_name)
    
    def append_to_add_on_modules_list(self, add_on_module) -> None:
        self.add_ons_modules.append(add_on_module)


    def welcome_message(self):
        print("----!Weclome to the Calculator!----")
        print("Type \"help\" for a list of commands")
    
    def take_command(self) -> None:
        self.command = input("\nEnter a command: ")
        self.commands.handle_command(self.command)

if __name__ == "__main__":
    calculator = Calculator()

    while calculator.program_running:
        calculator.take_command()