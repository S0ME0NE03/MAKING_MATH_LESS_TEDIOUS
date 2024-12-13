class Commands:
    def __init__(self):
        exit_key_words = []



        commands_dictionary = {
            "quit": self.exit_program
        }

    def execute(self, command: str):
        command_parts = command.split() #Used for multi worded commands such as "Download example.txt"
        base_command = command_parts[0] #The base command. Using last example, it would be "Download"

        if command == "quit" or command == "exit" or command == "break":
            self.exit_program()

        elif base_command == "multiply":
            self.multiply(command_parts[1:])
        else:
            print(f"Unknown command: {base_command}")
        
        dictionary = {"quit": self.exit_program()}
        dictionary.get("quit")


    def multiply(self, args: list[str]):
        """Perform a multiplication."""
        try:
            num1, num2 = map(float, args)
            print(f"Result: {num1 * num2}")
        except ValueError:
            print("Invalid arguments for multiplication. Please provide two numbers.")

    def exit_program(self):
        print("Exiting the program...")
        # self.calculator.program_running = False

# class Commands:
#     def execute(command : str):
#         pass



#     def quit_calculator():
#         quit()
    
#     def update():
#         pass

#     def download_from_github():
#         pass

#     def delete_add_on():
#         pass

