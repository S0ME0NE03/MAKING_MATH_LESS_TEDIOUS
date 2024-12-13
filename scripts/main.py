import importlib
import os
import sys

from file_manager import FileManager
from commands import Commands

class Calculator:
    def __init__(self) -> None:
        self.set_up_system_variables()

        self.welcome_message()
        self.main()
    
    def set_up_system_variables(self):
        self.MAIN_PROGRAM_PATH : str = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.program_running : bool = True

        self.set_up_add_ons()

    def set_up_add_ons(self):
        self.ADD_ONS_PATH : str = os.path.join(self.MAIN_PROGRAM_PATH, "add_ons")

        if not file_manager.folder_exits(self.ADD_ONS_PATH):
            file_manager.create_folder(folder_name="add_ons", folder_path = self.MAIN_PROGRAM_PATH)

        self.add_ons_list : list[str] = file_manager.fetch_files_in_path(self.ADD_ONS_PATH)

        if self.ADD_ONS_PATH not in sys.path:
            sys.path.append(self.ADD_ONS_PATH)

        self.add_ons_modules = []
        for filename in os.listdir(self.ADD_ONS_PATH):
            if filename.endswith('.py'):
                module_name = filename[:-3]  # Strip the .py extension
                try:
                    module = importlib.import_module(module_name)
                    self.add_ons_modules.append(module)

                except ImportError as e:
                    print(f"Error importing {module_name}: {e}")

    def welcome_message(self):
        print("----!Weclome to the Calculator!----")

    def main(self) -> None:
        while self.program_running:
            command = input("Enter a command: ")
            commands.execute(command)

if __name__ == "__main__":
    file_manager = FileManager()
    commands = Commands()
    Calculator()
