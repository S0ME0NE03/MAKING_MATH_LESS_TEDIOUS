while 1:
  ip = input("what do you want to run(prime factor, childern in basement calclulator)')
  if ip == "prime factor":
      exec(open("prime_factor.py").read())

  elif ip == "childern in basement calclulator":
    exec(open("children_in_basement_calc.py").read())
