import os
import requests
import importlib

#Some problems with the updateing function

class Commands:
    def __init__(self, calculator):
        self.calculator = calculator

        #Construct the custom commands name mapping
        self.add_ons_command_dict = {}
        for add_on_name, add_on_module in zip(calculator.add_ons_foldername_list, calculator.add_ons_modules): # I have no clue why or what zip() is doing here but it works
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
            "del": self.delete_add_on,
            "log": self.manual_user_log,
            "add_ons": self.display_add_ons,
            "view": self.view,
            "debug": self.debug
        }

        self.command_descriptions = {
            "quit": "Exits the program",
            "exit": "Exits the program",
            "help": "Displays a list of commands. (Extensions: command_name)",
            "clear": "Clears the specified extension. (Extensions: logs)",
            "update": "Updates the extension. (Extensions: add_on_name)",
            "download": "Downloads a new add on from github. (Extensions: add_on_name)",
            "del": "Deletes an add on (Extensions: add_on_name)",
            "log": "Manually logs a message",
            "add_ons": "Displays all installed add ons",
            "view": "Lets you view things. (Extensions: logs, add_ons, server_add_ons)",
            "debug": "Enters debug mode."
        }
    
    def fetch_add_on_names_from_git_hub_add_ons_folder(self) -> list[dict]:
        "Return a list of json as dictionaries withing in add_ons server folder"
        try:
            response = requests.get(self.calculator.api_url)
            response.raise_for_status()

            add_ons_in_server_add_ons_folder : list[dict] = response.json()

            add_ons: list[dict] = []
            for add_on in add_ons_in_server_add_ons_folder:
                if add_on["type"] == "dir" and (add_on["name"] not in self.calculator.system_ignore):
                    add_ons.append(add_on)

            return add_ons

        except Exception as error:
            print(f"An error occured while trying to get files from the server: {error}")
            self.calculator.program_logging.error_log(str(error))

    def update_add_ons_command_dict_if_req(self, add_on_name, add_on_module):
        if add_on_name in self.calculator.add_ons_foldername_list:
            self.add_ons_command_dict.update({add_on_name: add_on_module})

    def command_extension_invalid(self, command_parts):
        print(f"\"{command_parts[1]}\" is an unrecognized extension for {command_parts[0]}")

    def command_has_extension(self, command_parts) -> bool:
        if len(command_parts) > 1:
            return True
        else:
            return False

    def handle_command(self, command):
        command_parts = command.split() #Used for multi worded commands such as "Download example.txt"
        base_command = command_parts[0]

        if base_command in self.core_commands_dict:
            #This is some extremely funky syntax, but it just calls the function of the command
            self.core_commands_dict[base_command](command_parts)
        
        elif command in self.add_ons_command_dict:
            self.add_ons_command_dict[command].main()
        
        else:
            print(f"-!The command \"{base_command}\" is not recognized!-")

    def quit_program(self, command_parts):
        if self.command_has_extension(command_parts):
            print(f"\"{command_parts[0]}\" has an extension when one is not needed")
            return

        print("Exiting the program...")
        self.calculator.program_running = False
    
    def commands_help(self, command_parts):
        if self.command_has_extension(command_parts):
            description = self.command_descriptions.get(command_parts[1])
            if description == None:
                self.command_extension_invalid(command_parts)
            else:
                print(description)
        
        else:
            #Description for all core commands, and help on how to run add ons
            print("\n--Heres a list of all commands--")
            for command, description in self.command_descriptions.items():
                print(f"-{command}: {description}")        

            print("\n--Heres a list of currently installed add ons--")
            for add_on_name in self.calculator.add_ons_foldername_list:
                print(f"-{add_on_name}")         

            print("-!To run add ons, you must enter the name of the add on as a command!-")
        
    def clear(self, command_parts):
        if not self.command_has_extension(command_parts):
            print(f"{command_parts[0]} requires an extension to run")
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
        def download_file(url, local_path):
            file = requests.get(url).json()
            file_content = requests.get(file["download_url"]).content

            with open(local_path, 'wb') as f:
                f.write(file_content)
            print(f"Downloaded file: {local_path}")
            
        def download_folder(folder_url, local_folder):
            # Make sure the local folder exists
            if not os.path.exists(local_folder):
                os.makedirs(local_folder)

            # Fetch folder contents (assuming the response is a JSON containing 'files' and 'folders')
            response = requests.get(folder_url)
            response.raise_for_status()  # Check for successful request
            folder_data = response.json()

            # Download each file in this folder
            for file_info in folder_data:
                if file_info['type'] == 'file':
                    file_url = file_info['url']
                    file_name = file_info['name']
                    file_path = os.path.join(local_folder, file_name)
                    download_file(file_url, file_path)

            # Recurse into each subfolder
            for subfolder_info in folder_data:
                if subfolder_info['type'] == 'dir':
                    subfolder_name = subfolder_info['name']
                    subfolder_url = subfolder_info['url']
                    subfolder_path = os.path.join(local_folder, subfolder_name)
                    download_folder(subfolder_url, subfolder_path)  # Recurse into subfolder

        if not self.command_has_extension(command_parts):
            print(f"{command_parts[0]} requires an extension to run")
            return
        
        add_on_name = command_parts[1]
        if not add_on_name in self.calculator.add_ons_foldername_list:
            print(f"No add on named \"{add_on_name}\" was found in the add_ons folder")
            return

        try:
            add_ons : list[dict] = self.fetch_add_on_names_from_git_hub_add_ons_folder()
            for add_on in add_ons:
                if add_on_name == add_on["name"]:
                    add_on_path = os.path.join(self.calculator.ADD_ONS_PATH, add_on_name)
                    download_folder(add_on["url"], add_on_path)

                    for module in self.calculator.add_ons_modules:
                        if module.__name__ == add_on_name:
                            importlib.reload(module)
                            break
                    
                    print(f"Add on \"{add_on_name}\" successfully updated!")
                    return
            
            else:
                print(f"Add on \"{add_on_name}\" does not exist on the server")

        except Exception as error:
            print(f"An error occured while trying to update the add on: {error}")
            self.calculator.program_logging.error_log(str(error))

        #Add an option to update the actual program itself, 
        #like calculator file_manager and whatever

    def download_from_github(self, command_parts):
        
        #EXTREMEMLY CLUNKY I KNOW, BUT ANYTHING TO GET THE JOB DONE FOR NOW
        def download_folder(folder_url, local_folder):
            # Make sure the local folder exists
            if not os.path.exists(local_folder):
                os.makedirs(local_folder)

            # Fetch folder contents (assuming the response is a JSON containing 'files' and 'folders')
            response = requests.get(folder_url)
            response.raise_for_status()  # Check for successful request
            folder_data = response.json()

            # Download each file in this folder
            for file_info in folder_data:
                if file_info['type'] == 'file':
                    file_url = file_info['url']
                    file_name = file_info['name']
                    file_path = os.path.join(local_folder, file_name)
                    download_file(file_url, file_path)

            # Recurse into each subfolder
            for subfolder_info in folder_data:
                if subfolder_info['type'] == 'dir':
                    subfolder_name = subfolder_info['name']
                    subfolder_url = subfolder_info['url']
                    subfolder_path = os.path.join(local_folder, subfolder_name)
                    download_folder(subfolder_url, subfolder_path)  # Recurse into subfolder
                
        def download_file(url, local_path):
            file = requests.get(url).json()
            file_content = requests.get(file["download_url"]).content

            with open(local_path, 'wb') as f:
                f.write(file_content)
            print(f"Downloaded file: {local_path}")

        if not self.command_has_extension(command_parts):
            print(f"{command_parts[0]} requires an extension to run")
            return
        
        add_on_name = " ".join(command_parts[1:]) # DO NOT REMOVE THE SPACE IN THE STRING HERE

        if add_on_name in self.calculator.add_ons_foldername_list:
            print(f"Add on \"{add_on_name}\" is already installed")
            confrim = input("\nWould you like to update it? (y/n): ")
            if confrim == "y":
                self.update(command_parts)
            else:
                pass
            return
        
        try:
            add_ons : list[dict] = self.fetch_add_on_names_from_git_hub_add_ons_folder()
            for add_on in add_ons:
                if add_on["name"] == add_on_name:
                    add_on_path = os.path.join(self.calculator.ADD_ONS_PATH, add_on_name)
                    download_folder(add_on["url"], add_on_path)

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
        if not self.command_has_extension(command_parts):
            print(f"{command_parts[0]} requires an extension to run")
            return
        
        add_on_name = command_parts[1]
        if add_on_name not in self.calculator.add_ons_foldername_list:
            print(f"No add on named \"{add_on_name}\" was found in the add_ons folder")
            return
        
        confirm = input(f"Are you sure you want to delete the add on \"{add_on_name}\"? (y/n): ")
        if confirm == "y":
            add_on_path = os.path.join(self.calculator.ADD_ONS_PATH, add_on_name)
            os.remove(add_on_path)
            self.calculator.add_ons_foldername_list.remove(add_on_name)
            self.calculator.add_ons_modules = [module for module in self.calculator.add_ons_modules if module.__name__ != add_on_name]
            del self.add_ons_command_dict[add_on_name]
            print(f"Add on \"{add_on_name}\" successfully deleted!")
        
        else:
            return

    def manual_user_log(self, command_parts):
        if self.command_has_extension(command_parts):
           text = "" 
           for i in range(len(command_parts)-1):
               text += command_parts[i+1] + " "
           self.calculator.program_logging.multi_purpose_log(text)
           print("Log successfully saved!")
        else:
            text = str(input("What would you like to log?: "))
            self.calculator.program_logging.multi_purpose_log(text)
            print("Log successfully saved!")
    
    def display_add_ons(self, command_parts):
        if self.command_has_extension(command_parts):
            print("Command does not require an extension")
            return
        
        if len(self.calculator.add_ons_foldername_list) == 0:
            print("There are no add ons currently installed")
            return
            
        else:
            print("Heres a list of currently installed add ons:")
            for add_on in self.calculator.add_ons_foldername_list:
                print(f"-{add_on}")
        
    def view(self, command_parts):
        if not self.command_has_extension(command_parts):
            print(f"{command_parts[0]} requires an extension to run")
            return

        command_extention = command_parts[1]

        if command_extention == "logs":
            with open(self.calculator.program_logging.PROGRAM_LOGS_PATH, "r") as reader:
                print(reader.read())
        
        elif command_extention == "add_ons":
            print("Heres a list of currently installed add ons:")
            if len(self.calculator.add_ons_foldername_list) == 0:
                print("There are no add ons currently installed")
                return

            else:
                for add_on in self.calculator.add_ons_foldername_list:
                    print(f"-{add_on}")
        
        elif command_extention == "server_add_ons":
            files : list[dict] = self.fetch_add_on_names_from_git_hub_add_ons_folder()

            print("\nHeres a list of available add ons:")
            for file in files:
                print(f"-{file["name"]}")
        
        else:
            self.command_extension_invalid(command_parts)
            return

    def debug(self, command_parts):
        if self.command_has_extension(command_parts):
            print(f"{command_parts[0]} does not require an extension to run")
            return

        print("--Entered debug mode--")
        try:
            command = input("Enter a debug command: ")
            eval(command)
        except Exception as error:
            print(f"An error occured while trying to debug: {error}")
            self.calculator.program_logging.error_log(str(error))
