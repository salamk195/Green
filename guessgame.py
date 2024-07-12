import random
Users_guess= int(input("enter your guess"))
random_guess= random.randint(1 , 100)
countscore = 0
if Users_guess == random_guess:
    print("You are correct")
    countscore += 1
else:
    print("You are wrong")
print(f"the number was {random_guess} your totalscore is {countscore}")
