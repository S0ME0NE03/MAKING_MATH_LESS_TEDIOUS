import importlib
import os
import sys

from file_manager import FileManager
from commands import Commands
from program_logging import logging

class Calculator:
    def __init__(self) -> None:
        #If you change the order of this it can break
        self.file_manager = FileManager(self)

        self.set_up_system_variables()
        self.welcome_message()

        self.program_logging = logging(self.file_manager, self.MAIN_PROGRAM_PATH)
        self.commands = Commands(self)
    
    def set_up_system_variables(self):
        self.MAIN_PROGRAM_PATH : str = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.program_running : bool = True
        self.command = None

        self.set_up_add_ons()

    def set_up_add_ons(self):
        self.ADD_ONS_PATH : str = os.path.join(self.MAIN_PROGRAM_PATH, "add_ons")

        if not self.file_manager.folder_exits(self.ADD_ONS_PATH):
            self.file_manager.create_folder(folder_name="add_ons", folder_path = self.MAIN_PROGRAM_PATH)
        
        if self.ADD_ONS_PATH not in sys.path:
            sys.path.append(self.ADD_ONS_PATH)

        self.add_ons_filename_list: list[str] = []
        self.add_ons_modules = []

        for filename in os.listdir(self.ADD_ONS_PATH):
            if filename.endswith('.py'):
                module_name = filename[:-3]  # Strip the .py extension
                try:
                    module = importlib.import_module(module_name)
                    if hasattr(module, 'main'):
                        self.add_ons_modules.append(module)
                        self.add_ons_filename_list.append(module_name)
                    else:
                        self.program_logging.error_log(f"Module \"{module_name}\" does not have a \"main\" function so it cannot be run by the launcher")
                except ImportError as e:
                    print(f"Error importing {module_name}: {e}")
        
    def welcome_message(self):
        print("----!Weclome to the Calculator!----")
        print("Type \"help\" for a list of commands")
    
    def main_loop(self) -> None:
        while self.program_running:
            self.command = input("\nEnter a command: ")

            command_parts = self.command.split() #Used for multi worded commands such as "Download example.txt"
            if len(command_parts) > 2:
                print("The command may only be 2 key words long")
                continue
                
            else:
                base_command = command_parts[0] #The base command. Using last example, it would be "Download"

                if base_command in self.commands.core_commands_dict:
                    #This is some extremely funky syntax, but it just calls the function of the command
                    self.commands.core_commands_dict[base_command](command_parts)
                
                elif base_command in self.commands.add_ons_command_dict:
                    self.commands.add_ons_command_dict[self.command].main()
                
                else:
                    print(f"-!The command \"{base_command}\" is not recognized!-")
                
if __name__ == "__main__":
    claculator = Calculator()
    claculator.main_loop()
