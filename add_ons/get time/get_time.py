from datetime import datetime

class GetTime:
    def __init__(self):

        self.future_plans = ["show current time, and also show time around the world, whereever you specify"]


        self.version = "1.0.0"
        self.add_on_author = "Op-25"

        self.add_on_running = True
        self.commands = GetTimeCommands(self)

        self.commands_dict = {
        "help": self.commands.get_help,
        "exit": self.commands.quit_program,
        "quit": self.commands.quit_program,
        "time": self.commands.get_time,
        "get_time": self.commands.get_time,
        "date": self.commands.get_date,
        "get_date": self.commands.get_date,
        "datetime": self.commands.get_date_time,
        "date_time": self.commands.get_date_time,
        "get_datetime": self.commands.get_date_time,
        "get_date_time": self.commands.get_date_time,
        "credits": self.commands.module_credit,
            }
        
        self.commands_help_dict = {
        "help": "Display a list of available commands",
        "exit": "Exit the Get Time add-on",
        "time": "Display the current time",
        "date": "Display the current date",
        "datetime": "Display the current date and time",
        "credits": "Display the author of the Get Time add-on",
            }
        
    def welcome_message(self):
        print("\n--!Welcome to Get Time Add-On--!")
        print("For a list of available commands, enter \'help\"")
        
    def take_command(self):
        command = input("\nEnter an command: ")

        if command not in self.commands_dict:
            print(f"\"{command}\" is not a valid command.")
            return

        if command in self.commands_dict:
            self.commands_dict[command]()

class GetTimeCommands:
    def __init__(self, time):
        self.time = time    

    def get_help(self):
        print("List of available commands:")
        for command in self.time.commands_help_dict:
            print(f"-{command}")

    def quit_program(self):
        self.time.add_on_running = False

    def get_time(self):
        print(datetime.now().strftime("%H:%M:%S"))

    def get_date(self):
        print(datetime.now().strftime("%Y-%m-%d"))

    def get_date_time(self):
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def module_credit(self):
        print(f"The \"{__name__}\" add on was authored by {self.time.add_on_author}")

def main():
    get_time = GetTime()
    get_time.welcome_message()

    while get_time.add_on_running:
        get_time.take_command()
