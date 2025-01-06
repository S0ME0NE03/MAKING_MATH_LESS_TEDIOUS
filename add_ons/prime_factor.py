PRIME_TO_CALC = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999
import time
import urllib.request
def download(url, filename):
  urllib.request.urlretrieve(url, filename)
def prime_scive(to_go_to: int) -> list[int]:
    primes = [1]
    try:
        #happens most of the time
        #this reads the list of prime numbers and puts them into a list
        #on secont thougt i have no clue how this actualy gets the data 
        f = open("primes.txt", "r")
        try:
            for x in f:
                primes.append(int(x))
        except:
            pass
        f.close()

    except:
        #first boot
        first_boot =  True
        download_preload = input("do you agree to dowload a preload list of primes from:\nhttps://raw.githubusercontent.com/srmalins/primelists/refs/heads/master/100primes.txt (y,n)\n")
        if download_preload == "y":
            download("https://raw.githubusercontent.com/srmalins/primelists/refs/heads/master/100primes.txt", "primes.txt")
        else:
            f = open("primes.txt", "a")
            f.write("2\n3\n5\n")
            f.close()
        f = open("primes.txt", "r")
        try:
            for x in f:
                primes.append(int(x))
        except:
            pass
        f.close()

    f = open("primes.txt", "a")
    #stores time of boot for automatic time based breaking
    start_time = time.time()
    countdown = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0]
    for i in range (primes[-1]+1, to_go_to):
        j = 0
        #inproves performace by 2x
        if i % 2 == 1:
            if i % 3 != 0:
                if i % 5 != 0:
                    #priem sive 
                    for n in range(len(primes)):
                        if i % primes[n] == 0:
                            j+=1
                    if j == 1:
                        primes.append(i)
                        f.write(str(i)+"\n")
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    if elapsed_time > 10:
                        a = i
                        break
    f.close
    print("Calculated primes up to: ")
    print(primes[-1])
    print(" ")
    return primes 


def prime_factor(number, primes):
    output = []
    while not(number in primes) or (number < (primes[-1]**2) and number > primes[-1]):
        for i in range(len(primes)):
            if number % primes[i] == 0:
                if not(primes[i] == 1):
                    output.append(primes[i])
                    number = number/primes[i]
    if number != 1:
        output.append(int(number))
    return output

def unfactor(strlist: str) -> int:
    temp = []
    a = ""
    output = 1
    not_last = False 
    for i in strlist:
        if i == "," or i == " ":  
            if not_last == False:
                try:
                   temp.append(int(a))
                except:
                    print("not a number")
                    return ""
                not_last = True
                a = ""
        else:
            a += i
            #print(a)
            not_last = False
    if a:
       try:
           temp.append(int(a))
       except:
           print("not a number")
           return ""
    #print(temp)
    for i in range(len(temp)):
        output *= temp[i]  
    return output
      
         
def is_this_prime(primes,  number):
   if number in primes:
      return True
   else:
      return False
def main():
  print("Booting...\nCalculating Pimes\n\n")
  print("__________________")
  print("\                 \ ")
  print("|\                 \ ")
  print("| \                 \ ")
  print("|  \                 \ ")
  print("|   |-----------------|")
  print("|   |                 | ")
  print("|   |      prime      | ")
  print("\   |                 |")
  print(" \  |    factorizer   |")
  print("  \ |       :)        |")
  print("   \|                 |")
  print("    |-----------------|\n")
  primes = prime_scive(PRIME_TO_CALC)
  #print(prime_factor(10, primes))
  #print(primes)
  while 1:
     inp = input("What would you like to do?(prime factor, unfactor, check if prime, or EXIT)\n")
     if inp == "EXIT":
          break
     elif inp == "factor" or inp == "prime factor":
          
        inp = input("Input a int\n") 
        try:
           inp = int(inp)
        except:
           print("invalid imput.\n")
        if type(inp) == int and inp < primes[-1]**2:
           print(prime_factor(inp, primes))
        else:
             print("Number too high please enter a vaiue below " + str(primes[-1]**2))
     elif inp == 'unfactor':
        inp = input("Input a list of factors seperated by a space \n") 
        print(unfactor(inp))
     elif inp == "check if prime":
        if is_this_prime(primes, input("input a nuber to check:\n")):
           print("yes it is prime")
        else:
           print("no it is not a prime")
     else:
        print("Please enter a valid command.\n")


   
