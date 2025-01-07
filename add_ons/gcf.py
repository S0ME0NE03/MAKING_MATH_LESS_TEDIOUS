
def gcf(a,b,c):
    for i in range(a*C):
      for j in range(b):
        if i*j == a*c and i+j == b:
          return [i,j]
          break
    return ["no soution"]
def main():
  print(gcf(input("enter, a: \n"),input("enter, b:\n"),input("enter, c\n")  
