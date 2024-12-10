#golden_ratio_calc.py
while 1:
  ip = input("what do you want to run(prime factor, childern in basement calclulator, golden ratio calclulator)\n")
  if ip == "prime factor":
      try:
        exec(open("prime_factor.py").read())
      except:
        print("prime_factor.py is not downloaded or not in the curent folder, please download the progam at: \nhttps://github.com/S0ME0NE03/MAKING_MATH_LESS_TEDIOUS/blob/main/prime_factor.py\n")
  elif ip == "childern in basement calclulator":
    try:
      exec(open("children_in_basement_calc.py").read())
    except:
      print("children_in_basement_calc.py is not downloaded or not in the curent folder, please download the progam at: \nhttps://github.com/S0ME0NE03/MAKING_MATH_LESS_TEDIOUS/blob/main/children_in_basement_calc.py\n")
  elif ip == "golden ratio calclulator":
    try:
      exec(open("golden_ratio_calc.py").read())
    except:
      print("golden_ratio_calc.py is not downloaded or not in the curent folder, please download the progam at: \nhttps://github.com/S0ME0NE03/MAKING_MATH_LESS_TEDIOUS/blob/main/golden_ratio_calc.py\n")
  else:
      print('not a avalible program')
  
