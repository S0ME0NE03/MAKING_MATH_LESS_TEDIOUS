from datetime import datetime

class GetTime:
    def __init__(self):
        self.add_on_author = "Op-25"
        self.add_on_running = True

        self.future_plans = ["show current time, and also show time around the world, whereever you specify"]

        self.commands_dict = {
        "exit": self.quit_program,
        "quit": self.quit_program,
        "time": self.get_time,
        "get_time": self.get_time,
        "date": self.get_date,
        "get_date": self.get_date,
        "datetime": self.get_date_time,
        "date_time": self.get_date_time,
        "get_datetime": self.get_date_time,
        "get_date_time": self.get_date_time
            }
        
    def take_command(self):
        command = input("Enter an command: ")

        if command in self.commands_dict:
            self.commands_dict[command]()
        
        else:
            print(f"{command} is not a valid command.")

    def quit_program(self):
        self.add_on_running = False

    def get_time(self):
        print(datetime.now().strftime("%H:%M:%S"))

    def get_date(self):
       print(datetime.now().strftime("%Y-%m-%d"))

    def get_date_time(self):
       print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def main():
    get_time = GetTime()

    while get_time.add_on_running:
        get_time.take_command()