#children in basement calculator 
#include how many children
#how many days you have been doing it for
#input a number of pitbulls in the basement 
#random chance of subtracting children (because of pitbulls)

#importing random numbers
import random as rand

#were asking how many children are kidnapped per day

print("__________________")
print("\                 \ ")
print("|\                 \ ")
print("| \                 \ ")
print("|  \                 \ ")
print("|   |-----------------|")
print("|   |    children     | ")
print("|   |      in         | ")
print("\   |    basement     |")
print(" \  |   calculator    |")
print("  \ |       :)        |")
print("   \|                 |")a
print("    |-----------------|")

print("")
print("")
print("")
print("")
children = int(input("How many children do you kidnap per day (on average)? "))

print("")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("")

#how many days they did it
days = int(input("How many days have you been doing this (on average)? "))

print("Chill calm down")

print("")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("")

#multiply the children and the number of days to get the total number of chilren in the basement
total = children * days

input("On average, you would have around " + str(total) + " children in your basement for now. ")

print("")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("")

#1 hungry pitbull would eat 2 children, but not all of them are hungry 
pitbulls = int(input("How many pitbulls did you unleash in the basement? "))
#coding and using formuler
#random number because not all pitbulls are hungry
nummy = rand.randint(0, pitbulls)

#one pitbull eats 2 kids
eat = nummy * 2 

#subtract the children from the eaten ones
final_children = total - eat

print("")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("")


#a different output will display whether there is children or no children in the basement.

if(0<final_children):
    print("After some pitbulls had their delicious snack of " + str(eat) + " children, there are " + str(final_children) + " children")
    print( "remaining in your basement.")
else: 
    print("There are no more childen in your basement; all of them were eaten by the pitbulls.")

print("")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("")

leave = rand.randint(0, pitbulls)

print("After the pitbulls yummy snack on children, " + str(leave) + " out of " + str(pitbulls) + " pitbulls decided to leave.")

print("")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("")

remain = pitbulls - leave

print("This means that " + str(remain) + " pitbulls remain in your basement.")
