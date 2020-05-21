from random import *
import string
guess = ""
password = input("enter password!!")
letters = string.ascii_lowercase
while(guess!=password):
    guess = ""
    for letter in password:
        guessletter = letters[randint(0,25)]
        guess = str(guessletter) + str(guess)
    #print(guess)
print("pasword cracked")
input("")
