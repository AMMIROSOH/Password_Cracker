import string
i = j = k = l = 0
guess1 = guess2 = guess3 = guess4 = ""
listlengh = 62
password = input("enter a password for example!!")
letters = string.ascii_letters
numbers = ["0","1","2","3","4","5","6","7","8","9"]
char = [""]
char.extend(letters)
char.extend(numbers)

while (i <= listlengh and guess4!=password):
    j = 0
    guess1 = ""
    guessletter = char[i]
    guess1 = str(guessletter)
    i+=1
    while (j <= listlengh and guess4!=password):
        k = 0
        guess2 = ""
        guessletter = char[j]
        guess2 = str(guess1) + str(guessletter)
        j+=1
        while (k <= listlengh and guess4!=password):
            l = 0
            guess3 = ""
            guessletter = char[k]
            guess3 = str(guess2) + str(guessletter)
            k+=1
            while (l <= listlengh and guess4!=password):
                guess4 = ""
                guessletter = char[l]
                guess4 = str(guess3) + str(guessletter)
                #print(guess4)#print all guessed passwords, it wastes time
                l+=1 
        
            
    
print("pasword cracked:",guess4)#print the correct one
input("")
