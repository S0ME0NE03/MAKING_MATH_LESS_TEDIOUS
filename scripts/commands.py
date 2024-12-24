import os
import requests

class Commands:
    def __init__(self, calculator):
        self.calculator = calculator

        #Construct the custom commands name mapping
        self.add_ons_command_dict = {}
        for add_on_name, add_on_module in zip(calculator.add_ons_filename_list, calculator.add_ons_modules): # I have no clue why or what zip() is doing here but it works
            self.update_add_ons_command_dict_if_req(add_on_name, add_on_module)
            
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
            "add_ons": self.display_add_ons,
            "view": self.view
        }

        self.command_descriptions = {
            "quit": "Exits the program",
            "exit": "Exits the program",
            "help": "Displays a list of commands. (Extensions: command_name)",
            "clear": "Clears the specified extension. (Extensions: logs)",
            "update": "Updates the extension. (extensions: to be implemented prolly module names)",
            "download": "Downloads a new add on from github. (Extensions: add_on_name)",
            "delete": "Deletes an add on (Extensions: add_on_name)",
            "log": "Manually logs a message",
            "add_ons": "Displays all installed add ons",
            "view": "Lets you view things. (Extensions: logs, add_ons, server_add_ons)"
        }
    
    def send_http_request_to_github_add_ons_folder(self) -> list[dict]:
        "Return a list of json as dictionaries withing in add_ons server folder"
        response = requests.get(self.calculator.api_url)
        response.raise_for_status()

        return response.json()
        
    def update_add_ons_command_dict_if_req(self, add_on_name, add_on_module):
        if add_on_name in self.calculator.add_ons_filename_list:
            self.add_ons_command_dict.update({add_on_name: add_on_module})

    def command_extension_invalid(self, command_parts):
        print(f"\"{command_parts[1]}\" is an unrecognized extension for {command_parts[0]}")

    def command_has_extension_with_error_msg(self, command_parts) -> bool:
        if self.command_has_extension(command_parts):
            print(f"{command_parts[0]} has an extension when one is not needed")
            return True
        else:
            print(f"{command_parts[0]} needs 1 command extension to run")
            return False
    
    def command_has_extension(self, command_parts) -> bool:
        if len(command_parts) > 1:
            return True
        else:
            return False

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

    def quit_program(self, command_parts):
        if self.command_has_extension(command_parts):
            print("Command does not require an extension")
            return

        print("Exiting the program...")
        self.calculator.program_running = False
    
    def commands_help(self, command_parts):
        if len(command_parts) == 1:
            #Description for all core commands, and help on how to run add ons
            print("\n--Heres a list of all commands--")
            for command, description in self.command_descriptions.items():
                print(f"-{command}: {description}")        

            print("\n--Heres a list of currently installed add ons--")
            for add_on_name in self.calculator.add_ons_filename_list:
                print(f"-{add_on_name}")         

            print("-!To run add ons, you must enter the name of the add on as a command!-")

        elif len(command_parts) == 2:
            description = self.command_descriptions.get(command_parts[1])
            if description == None:
                self.command_extension_invalid(command_parts)
            else:
                print(description)
        
    def clear(self, command_parts):
        if not self.command_has_extension_with_error_msg(command_parts):
            return
        
        extension = command_parts[1]

        if extension == "logs":
            confirm = input("Are you sure you want to clear all logs? (y/n): ")
            if confirm == "y":
                self.calculator.program_logging.clear_logs()
                print("Logs have been cleared!")
            else:
                print("Logs have not been cleared")

            return
        
        elif extension == None or extension == "cls":
            #os.system(clear) Im hesitent on this because it may not work on all systems like windows vs linux stuff
            pass

        else:
            self.command_extension_invalid(command_parts)
            return
    
    def update(self, command_parts):
        pass
        # Go on the github page and redownload the desired file
        # Shold be quite simple because I can use filemanager to delete file and create
        # Use requests.get for this

    def download_from_github(self, command_parts):
        if not self.command_has_extension_with_error_msg(command_parts):
            return
        
        add_on_name = command_parts[1]
        
        if add_on_name in self.calculator.add_ons_filename_list:
            print(f"Add on \"{add_on_name}\" is already installed!")
            return
        
        try:
            files : list[dict] = self.send_http_request_to_github_add_ons_folder()

            for file in files:
                if add_on_name == file["name"][:-3]:
                    add_on_in_correct_dir = os.path.join(self.calculator.ADD_ONS_PATH, add_on_name + ".py")
                    file_content = requests.get(file["download_url"]).content

                    with open(add_on_in_correct_dir, "wb") as writer:
                        writer.write(file_content)

                    self.calculator.program_logging.file_created_log(add_on_name, self.calculator.ADD_ONS_PATH)

                    self.calculator.update_add_ons_modules_if_req_met(add_on_name)
                    self.update_add_ons_command_dict_if_req(add_on_name, self.calculator.add_ons_modules[-1])

                    print(f"Add on \"{add_on_name}\" successfully downloaded!")
                    return
            else:
                print(f"Add on \"{add_on_name}\" does not exist on the server")
                return
            
        except Exception as error:
            print(f"An error occured while trying to download the add on: {error}")
            self.calculator.program_logging.error_log(str(error))

    def delete_add_on(self, command_parts):
        pass

    def manual_user_log(self, command_parts):
        if self.command_has_extension_with_error_msg(command_parts):
            return
        
        else:
            text = str(input("What would you like to log?: "))
            self.calculator.program_logging.multi_purpose_log(text)
            print("Log successfully saved!")
    
    def display_add_ons(self, command_parts):
        if self.command_has_extension:
            print("Command does not require an extension")
            return
        
        if len(self.calculator.add_ons_filename_list) == 0:
            print("There are no add ons currently installed")
            return
            
        else:
            for add_on in self.calculator.add_ons_filename_list:
                print(f"-{add_on}")
        
    def view(self, command_parts):
        if not self.command_has_extension_with_error_msg(command_parts):
            return

        command_extention = command_parts[1]

        if command_extention == "logs":
            with open(self.calculator.program_logging.PROGRAM_LOGS_PATH, "r") as reader:
                print(reader.read())
        
        elif command_extention == "add_ons":
            if len(self.calculator.add_ons_filename_list) == 0:
                print("There are no add ons currently installed")
                return

            else:
                for add_on in self.calculator.add_ons_filename_list:
                    print(f"-{add_on}")
        
        elif command_extention == "server_add_ons":
            files : list[dict] = self.send_http_request_to_github_add_ons_folder()

            print("\nHeres a list of available add ons:")
            for file in files:
                print(f"-{file["name"][:-3]}")
        
        else:
            self.command_extension_invalid(command_parts)
            return