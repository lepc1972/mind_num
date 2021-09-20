#  module that let us choice random numbers
import random
# module for figlet
import pyfiglet

result = pyfiglet.figlet_format("WELCOME TO MASTERMIND")
print(result)
result1 = pyfiglet.figlet_format("BY")
print(result1)
result2 = pyfiglet.figlet_format("LEPC")
print(result2)

# group of allow numbers for this mastermind
digits = ('0','1','2','3','4','5','6','7','8','9')

# the code 
numb_of_digits = 4
code = ''
for i in range(numb_of_digits):
    cand = random.choice(digits)
    # here we choose not equal digits
    while cand in code:
        cand = random.choice(digits)
    code = code + cand

# user interaction
name = input("Here...your name:" )
print ( name, "Welcome to Mastermind!")
print ("You have to guess a number of", numb_of_digits, 
      "different digits")
your_code = input("So...tell me your code: ")

# here we proccess hits, matches and attempts

attempt = 0
while your_code != code and your_code != "F...":
    attempt = attempt + 1
    hits = 0
    matches = 0

    # we travel around around of your code
    for i in range(numb_of_digits):
        if your_code[i] == code[i]:
            hits = hits + 1
        elif your_code[i] in code:
            matches = matches + 1
    print ("Your code ", your_code, " have", hits, \
        "hits ", matches, "matches and", attempt, "attempts")
# here we ask for a new code
    your_code = input("try an other code: ")

if your_code == "F...":
    print ("The code is", code)
    print (name, "you got", hits, "hits", matches, "matches  in", 
    attempt, "attempts" )
    
    print ("Better luck next time")
else:
    print ("Congrats...you did it in" ,attempt , "attempts")
