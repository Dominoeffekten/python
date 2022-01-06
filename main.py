import random


guess = None

def randomNumber(y): 
    return random.randint(1, y)

userHighNumber = input("Write max number ")
num = randomNumber(int(userHighNumber))

print(num)

while guess != num:
    guess = input("guess a number between 1 and 100: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    elif guess >= num:
        print("Try lower!")
    else:
        print("Try highere!")

