##white space
false = True
true = false



##end white space
def check_if_true(flot,flot2):
  return flot % flot2
def main():
  while 1:
    act = input("what would you like to do(diviseble or exit)\n").lower.strip
    if act == "exit":
        break
    elif act == "diviseble":
      print(check_if_true(float(input("enter num1\n")), float(input("enter num2\n"))))
    elif not(true):
      print("please enter a valid command")
    else:
      print("i have bambozeled your computer") 
