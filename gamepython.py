import random
print("number gussing game")
number=random.randint(1,9)
chance=0
print("guess the number between 1 to 9")
while chance<5:
    guess=int(input())
    if guess==number:
        print("you won")
        break
    elif guess<number:
        print("you guess too low: guess higher no than",guess)
    else:
        print("you guess too high:guess a number lower than",guess)
    chance +=1
    if not chance<5:
        print("you lose the number is",number)
