#is there a more secure way of doing this
def main():
    print("Enter \"exit\" to exit")
    while True:
        action = input(": ")

        if action == "quit" or action == "exit":
            break
            
        else:
            try:
                print(eval(action))
            except Exception as error:
                print(f"Error: {error}")
