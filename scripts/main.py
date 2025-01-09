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
        self.GITHUB_ADD_ONS_URL : str = "https://github.com/S0ME0NE03/MAKING_MATH_LESS_TEDIOUS/tree/main/add_ons"
        self.api_url : str = "https://api.github.com/repos/S0ME0NE03/MAKING_MATH_LESS_TEDIOUS/contents/add_ons"

        self.repo_owner = "S0ME0NE03"  # Replace with the repository owner
        self.repo_name = "MAKING_MATH_LESS_TEDIOUS"  # Replace with your repository name

        self.program_running : bool = True
        self.command = None

    def set_up_add_ons(self):
        self.ADD_ONS_PATH : str = os.path.join(self.MAIN_PROGRAM_PATH, "add_ons")
        self.add_ons_foldername_list: list[str] = []
        self.add_ons_modules = []

        if self.ADD_ONS_PATH not in sys.path:
            sys.path.append(self.ADD_ONS_PATH)

        if not self.file_manager.folder_exits(self.ADD_ONS_PATH):
            self.file_manager.create_folder(folder_name="add_ons", folder_path = self.MAIN_PROGRAM_PATH)
            
        for folder_name in os.listdir(self.ADD_ONS_PATH):
            self.update_add_ons_modules_if_req_met(folder_name)
    
    def update_add_ons_modules_if_req_met(self, folder_name) -> None:
        # if file_name.endswith('.py'):
        module_name = folder_name  # Strip the .py extension
        try:
            module = importlib.import_module(f"{module_name}/main.py")
            if hasattr(module, 'main'):
                self.add_ons_modules.append(module)
                self.add_ons_filename_list.append(module_name)
            else:
                self.program_logging.error_log(f"Module \"{module_name}\" does not have a \"main\" function so it cannot be run by the launcher")
        except ImportError as e:
            self.program_logging.error_log(f"Error importing {module_name}: {e}")
    else:
        if file_name == "__pycache__":
            return
        else:
            self.program_logging.error_log(f"File \"{file_name}\" is not a python file so it cannot be imported")

    def welcome_message(self):
        print("\n----!Weclome to the Calculator!----")
        print("Type \"help\" for a list of commands")
    
    def take_command(self) -> None:
        self.command = input("\nEnter a command: ")
        self.commands.handle_command(self.command)

if __name__ == "__main__":
    calculator = Calculator()

    while calculator.program_running:
        calculator.take_command()
