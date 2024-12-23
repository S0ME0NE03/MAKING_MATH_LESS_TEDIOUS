import os
from datetime import datetime

class logging:
    def __init__(self, calculator):
        self.calculator = calculator

        self.PROGRAM_LOGS_PATH = self.calculator.MAIN_PROGRAM_PATH + "/program_logs.txt"

        self.check_for_logging_file()
        self.program_launcher_log()

    def check_for_logging_file(self):
        # I cant use FileManager here because it would create a circular import
        # Which I hate so much because you should almost never repeat yourlsef ever

        file_name = "program_logs.txt"
        file_path = self.calculator.MAIN_PROGRAM_PATH
        
        if not os.path.isfile(self.PROGRAM_LOGS_PATH):
            try:
                created_file = open(f"{file_path}/{file_name}", "x")
                self.file_created_log(file_name, file_path)
                created_file.close()

            except Exception as error:
                print("Something went wrong! " + str(error))
                self.error_log(str(error))

    def get_time(self):
        return datetime.now()

    def append_to_file(self, content_format):
        with open(self.PROGRAM_LOGS_PATH, "a") as writer:
            writer.write(content_format + "\n")

    def multi_purpose_log(self, anything: str):
        content_format = f"{self.get_time()}: !MULTI-PURPOUSE LOG!: -> {str(anything)}"
        self.append_to_file(content_format)
    
    def file_created_log(self, file, path):
        content_format = f"{self.get_time()}: !FILE CREATED!: -> New file \"{file}\" created at {path}"
        self.append_to_file(content_format)
        
    def folder_created_log(self, folder, path):
        content_format = f"{self.get_time()}: !FOLDER CREATED!: -> New file \"{folder}\" created at {path}"
        self.append_to_file(content_format)

    def error_log(self, error: str):
        content_format = f"{self.get_time()}: !ERROR!: -> {str(error)}"
        self.append_to_file(content_format)
    
    def program_launcher_log(self):
        content_format = f"{self.get_time()}: !BOOT!: -> The aplication was run"
        self.append_to_file(content_format)

    def clear_logs(self):
        file = open(self.PROGRAM_LOGS_PATH, "w")
        file.close()