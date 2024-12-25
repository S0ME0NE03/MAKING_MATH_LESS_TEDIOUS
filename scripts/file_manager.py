import os

class FileManager:
    def __init__(self, calculator):
        self.calculator = calculator

    def file_exists(self, file_path: str) -> bool:
        return os.path.isfile(file_path)
    
    def folder_exits(self, folder_path : str) -> bool:
        return os.path.isdir(folder_path)
    
    def create_file(self, file_name : str, file_path : str) -> None:
        #Maybe refactor this so you can have more control like if "x", "w", or "wb"  or whatever
        try:
            created_file = open(f"{file_path}/{file_name}", "x")
            created_file.close()

            self.calculator.program_logging.file_created_log(file_name, file_path)
            
        except Exception as error:
            print("Something went wrong! " + str(error))
            self.calculator.program_logging.error_log(str(error))
    
    def update_file(self, file_path : str, file_name : str, content : str, mode : str) -> None:
        try:
            with open(f"{file_path}/{file_name}", mode) as writer:
                writer.write(content)
            
            self.calculator.program_logging.file_updatedlog(file_name, file_path)
            
        except Exception as error:
            print("Something went wrong! " + str(error))
            self.calculator.program_logging.error_log(str(error))

    def create_folder(self, folder_name: str, folder_path: str) -> None:
        try:
            if not os.path.isdir(folder_path):
                raise FileNotFoundError(f"The specified folder path does not exist: {folder_path}")

            full_path = os.path.join(folder_path, folder_name)

            if os.path.exists(full_path):
                print(f"The folder '{folder_name}' already exists in '{folder_path}'.")
                return

            os.mkdir(full_path)
            self.calculator.program_logging.folder_created_log(folder_name, folder_path)

        except FileNotFoundError as fnfe:
            print(f"Error: {fnfe}")
            self.calculator.program_logging.error_log(str(fnfe))
            
        except Exception as error:
            print(f"Something went wrong: {error}")
            self.calculator.program_logging.error_log(str(error))
    
    def delete_folder(self, folder_path:str ):
        if not os.path.exists(folder_path):
            self.calculator.program_logging.error_log(f"Folder '{folder_path}' does not exist.")
            return
        
        try:
            # Walk through all files and subdirectories
            for root, dirs, files in os.walk(folder_path, topdown=False):
                # Delete files
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)

                # Delete empty directories
                for directory in dirs:
                    dir_path = os.path.join(root, directory)
                    os.rmdir(dir_path)

            # Delete the root folder itself
            os.rmdir(folder_path)
            self.calculator.program_logging.multi_purpose_log(f"Deleted folder '{folder_path}'.")
        except Exception as e:
            print(f"Error deleting folder '{folder_path}': {e}")

    def fetch_files_in_path(self, path: str) -> list[str]:
        try:
            files : list[str] = []
            for file in os.listdir(path):
                if os.path.isfile(os.path.join(path, file)):
                    files.append(file)
            return files
        
        except Exception as error:
            print("Something went wrong!: " + str(error))
            self.calculator.program_logging.error_log(str(error))