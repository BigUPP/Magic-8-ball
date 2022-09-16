import random
import time 
randomnumber = random.randint(1, 5)
playAgain = "y"

name = input("what is your name? ")
while name.isdigit():
    name = input("what is your name? ")
    print("hello " + name)             
    time.sleep(1)
while playAgain == "y" or playAgain == "yes":
    input("what is your question? ")

    randomnumber = random.randint(1, 5)

    
    if randomnumber == 1:
        print(name,"... you will be dead soon.")
    elif randomnumber == 2:
        print(name,"...you will trip and fall in the next 5 minutes before failing your upcoming quiz/test")
    elif randomnumber == 3:
        print(name,"... you'll gain imoratility")
    elif randomnumber == 4:
        print(name,"... you will recive 3 dollars")
    elif randomnumber == 5:
        print(name,"... you will be unlucky")
    elif randomnumber == 6:
        print(name,"... you will be dead soon.")
    elif randomnumber == 7:
        print(name,"...you will trip and fall in the next 5 minutes before failing your upcoming quiz/test")
    elif randomnumber == 8:
        print(name,"... you'll gain imoratility")
    elif randomnumber == 9:
        print(name,"... you will recive 3 dollars")
    elif randomnumber == 10:
        print(name,"... you will be unlucky")
    elif randomnumber == 11:
        print(name,"... you got the ultra rare fortune, consider yourself lucky!")
    time.sleep(2)
    playAgain = input("play again? y/n")

print("thank you so much for to playing my game")
time.sleep(1)
quit()
