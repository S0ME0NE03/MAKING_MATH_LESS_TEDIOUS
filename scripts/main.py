from file_manager import FileManager

class Calculator:
    def __init__(self) -> None:
        self.set_up_system_variables()

        self.welcome_message()
        self.main()
    
    def set_up_system_variables(self):
        self.MAIN_PROGRAM_PATH : str = "../" # Relative path to the scripts folder
        self.program_running : bool = True
        self.command : str = None

        self.set_up_add_ons()

    def set_up_add_ons(self):
        self.add_ons_path : str = "../add_ons" # This is relative path
        if file_manager.folder_exits(self.add_ons_path) == False:
            file_manager.create_folder(folder_name="add_ons", folder_path = self.MAIN_PROGRAM_PATH)

        self.add_ons_list : list[str] = file_manager.fetch_files_in_path(self.add_ons_path)

    def welcome_message(self):

        print("----!Weclome to the Calculator!----")

    def main(self) -> None:
        while self.program_running:
            self.command = input("Enter a command: ")
            if self.command in self.add_ons_list:
                pass
                # Run main from the targeted file. Ex, self.command.main() or the like
            
        else:
            print("Program Quit")

if __name__ == "__main__":
    file_manager = FileManager()
    Calculator()