from random import randint

number = randint(1, 100)
print("Guess the number between 1 to 100")
chances = int(input("No. of chances you wanna take: "))

while chances:
    response = int(input("your guess: "))
    if response == number:
        print("You Guessed it right in {} chances".format(chances))
        break
    elif response > number:
        print("You guessed it a bit higher")
    else:
        print("You guessed it a bit lower")
    chances -= 1
else:
    print("you lose! The number was", number)
