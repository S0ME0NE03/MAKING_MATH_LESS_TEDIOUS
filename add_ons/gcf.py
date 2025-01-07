
def gcf(a,b,c):
    for i in range(a*C):
      for j in range(b):
        if i*j == a*c and i+j == b:
          return [i,j]
    return ["no soution"]
def main():
  print(gcf(int(input("enter, a: \n")),int(input("enter, b:\n")),int(input("enter, c\n"))))  
