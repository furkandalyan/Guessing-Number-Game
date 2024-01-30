import random

import time


print("Guess a number betwween 1 to 100")
 
tru_num=random.randint(1,100)
right_to_guess=5

while True:
    guess_num=int(input("Enter your guess:"))

    if guess_num<tru_num:
        print("Controling number.....")
        time.sleep(3)

        print("Guess larger value"),
        right_to_guess=right_to_guess-1
        
        

    elif guess_num>tru_num:
        print("Controlling number......")
        time.sleep(3)

        print("Guess smaller value")
        right_to_guess=right_to_guess-1

        
    

    
    elif guess_num==tru_num:
        print("Controlling number.....")
        time.sleep(3)

        print("Your guess is correct!")
        break
    
    
    elif right_to_guess==0:
        break
    
    
print(tru_num,right_to_guess)


    

