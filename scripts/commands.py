import os
import urllib.request
import importlib

class Commands:
    def __init__(self, calculator):
        self.calculator = calculator

        #Construct the custom commands name mapping
        self.add_ons_command_dict = {}
        for add_on_name, add_on_module in zip(calculator.add_ons_filename_list, calculator.add_ons_modules): # I have no clue why or what zip() is doing here but it works
            self.add_ons_command_dict.update({add_on_name: add_on_module})

        #Please try an keep these in order
        #These all have to be one word bases
        self.core_commands_dict = {
            "quit": self.quit_program,
            "exit": self.quit_program,
            "help": self.commands_help,
            "clear": self.clear,
            "update": self.update,
            "download": self.download_from_github,
            "delete": self.delete_add_on,
            "log": self.manual_user_log,
            "add": self.display_add_ons,
            "view": self.view
        }

        self.command_descriptions = {
            "quit": "Exits the program",
            "exit": "Exits the program",
            "help": "Displays a list of commands",
            "clear": "Clears logs or the terminal",
            "update": "Updates the program",
            "download": "Downloads a new add on from github",
            "delete": "Deletes an add on",
            "log": "Manually logs a message",
            "add": "Displays all add ons",
            "view": "Lets you view things"
        }
    
    def handle_command(self, command):
        command_parts = command.split() #Used for multi worded commands such as "Download example.txt"

        if len(command_parts) > 2: #Something like this may change later, but I doubt it
            print("The command may only be 2 key words long")
            return
        
        base_command = command_parts[0] #The base command. Using last example, it would be "Download"

        if base_command in self.core_commands_dict:
            #This is some extremely funky syntax, but it just calls the function of the command
            self.core_commands_dict[base_command](command_parts)
        
        elif base_command in self.add_ons_command_dict:
            self.add_ons_command_dict[command].main()
        
        else:
            print(f"-!The command \"{base_command}\" is not recognized!-")

    def command_extension_invalid(self, args):
        print(f"\"{args[1]}\" is an unrecognized extension for {args[0]}")

    def command_needs_extension_checker(self, args):
        if len(args) < 2:
            print(f"{args[0]} needs 1 command extension to run")
            return False
        
        else:
            return True
    
    def quit_program(self, args):
        if len(args) > 1:
            print("To quit the program simply type \"quit\" or \"exit\"")
            return
        else:
            print("Exiting the program...")
            self.calculator.program_running = False
    
    def commands_help(self, args):
        if len(args) == 1:
            #Description for all core commands, and help on how to run add ons
            print("\n--Heres a list of all commands--")

            for command, description in self.command_descriptions.items():
                print(f"{command}: {description}")        

            print("\n--Heres a list of currently installed add ons--")

            for add_on_name in self.calculator.add_ons_filename_list:
                print(add_on_name)         

            print("-!To run add ons, you must enter the name of the add on as a command!-")

        else:
            description = self.command_descriptions.get(args[1])
            if description == None:
                self.command_extension_invalid(args)

            else:
                print(description)
    
    def clear(self, args):
        if not self.command_needs_extension_checker(args):
            return

        if args[1] == "logs":
            confirm = input("Are you sure you want to clear all logs? (y/n): ")
            if confirm == "y":
                self.calculator.program_logging.clear_logs()
                print("Logs have been cleared!")
            else:
                print("Logs have not been cleared")
                return
        
        elif args[1] == None:
            #os.system(clear) Im hesitent on this because it may not work on all systems like windows vs linux stuff
            pass

        else:
            self.command_extension_invalid(args)
            return
    
    def update(self, args):
        pass

    def download_from_github(self, args):
        if not self.command_needs_extension_checker(args):
            return
        
        add_on_name = args[1]
        
        if add_on_name in self.calculator.add_ons_filename_list:
            print(f"Add on \"{add_on_name}\" is already installed!")
            return
        
        #might use later if I wanna change for whatever reason
        # add_on_name = input("Enter the name of the add on you would like to download (without .py extension): ")
        add_ons_path_with_new_file = os.path.join(self.calculator.ADD_ONS_PATH, add_on_name + ".py")

        try:
            urllib.request.urlretrieve(f"{self.calculator.GITHUB_ADD_ONS_URL_RAW}/{add_on_name}.py", add_ons_path_with_new_file)
            #I can reuse somo calculator class code here, but i would need to refactor it
            # gonna have to refactor this bit and some other code for new add ons to work with existing variables
            self.calculator.add_ons_filename_list.append(add_on_name)
            self.calculator.add_ons_modules.append(importlib.import_module(add_on_name))
            self.add_ons_command_dict.update({add_on_name: self.calculator.add_ons_modules[-1]})

            self.calculator.program_logging.file_created_log(add_on_name, self.calculator.ADD_ONS_PATH)
            print(f"Add on \"{add_on_name}\" successfully downloaded!")
        except Exception as error:
            print(f"An error occured while trying to download the add on: {error}")
            self.calculator.program_logging.error_log(str(error))

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
    
    def display_add_ons(self, args):
        if not self.command_needs_extension_checker(args):
            return

        if args[1] == "ons":
            for add_on in self.calculator.add_ons_filename_list:
                print(add_on)
        
        else:
            self.command_extension_invalid(args)

    def view(self, args):
        if not self.command_needs_extension_checker(args):
            return

        if args[1] == "logs":
            with open(self.calculator.program_logging.PROGRAM_LOGS_PATH, "r") as reader:
                print(reader.read())
        
        else:
            self.command_extension_invalid(args)
    
    def show_currently_aviable_add_ons(self):
        pass
        #Idk how to do this rn, but the logic is gonna be get acess to the github page and go
        #into the scripts folder. Now create a new list of avalivble files from all files on the add ons folder