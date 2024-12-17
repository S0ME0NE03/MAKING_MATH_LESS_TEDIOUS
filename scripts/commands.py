import os

class Commands:
    def __init__(self, calculator):
        self.calculator = calculator

        #Construct the custom commands name mapping
        self.add_ons_command_dict = {}
        for add_on_name, add_on_module in zip(calculator.add_ons_filename_list, calculator.add_ons_modules): # I have no clue why or what zip() is doing here but it works
            self.add_ons_command_dict.update({add_on_name: add_on_module})

        #Please try an keep these in order
        self.core_commands_dict = {
            "quit": self.quit_program,
            "exit": self.quit_program,
            "help": self.commands_help,
            "clear": self.clear,
            "update": self.update,
            "download": self.download_from_github,
            "delete": self.delete_add_on,
            "log": self.manual_user_log
        }
        
    def quit_program(self, args):
        if len(args) > 1:
            print("To quit the program simply type \"quit\" or \"exit\"")
            return

        else:
            print("Exiting the program...")
            self.calculator.program_running = False
    
    def commands_help(slef, args):
        if len(args) == 1:
            #Description for all core commands, and help on how to run add ons
            print("Command descriptions are to be added")
        
        else:
            #In the future, use arg[1] for help on a specific command
            pass
    
    def clear(self, args):
        if len(args) < 2:
            print("Clear needs 1 command extension to run. Did you mean \"clear logs\"?")
            return

        if args[1] == "logs":
            self.calculator.program_logging.clear_logs()
            print("Logs have been cleared!")
        
        elif args[1] == None:
            #os.system(clear) Im hesitent on this because it may not work on all systems like windows vs linux stuff
            pass

        else:
            print(f"\"{args[1]}\" is an unrecognized argument for clear")
            return
    
    def update(self, args):
        pass

    def download_from_github(self, args):
        pass

    def delete_add_on(self, args):
        pass

    def manual_user_log(self, args):
        if len(args) > 1:
            print("Log does not need any command extentions/arguments")
            return
        else:
            text = str(input("What would you like to log?: "))
            self.calculator.program_logging.multi_purpose_log(text)
            print("Log successfully saved!")
