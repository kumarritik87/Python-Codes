import random
repeat = True
while repeat:
    m = random.randint(1,6)
    n = int(input("Guess a number between 1 to 6\n"))
    if m == n:
        print("Congratulation, you guess a right answer")
    else :
        print("Your answer is wrong")
        
    
