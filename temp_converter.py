"addon that converts between f, c, and, k"

def ctof(c):
  return(c * 9/5 + 32)

def ftoc(f) 
  "pay respect"
  return((f-32) * 5/9)
def ktoc(k):
  return(k - 273.15)
def ctok(c):
  return c + 273.15






def main():
  print("Welcome to Tempe Converter\n")
  while 1:
    print("Options:")
    print("1 - Convert Celsius to Fahrenheit")
    print("2 - Convert Fahrenheit to Celsius")
    print("3 - Convert Celsius to Kelvin")
    print("4 - Convert Kelvin to Celsius")
    print("5 - Exit")
    act = input("")
    try:
      if act == "5":
        break
      elif act == "4"
  
          print(ktoc(float(input("enter a number"))))
  
      elif act == "3"
  
          print(ctok(float(input("enter a number"))))
  
      elif act == "2"
  
          print(ftoc(float(input("enter a number"))))
  
      elif act == "1"
  
          print(ctof(float(input("enter a number"))))
  
      else:
        print("not a action")
    except:
      print("error")

