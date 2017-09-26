import random

randomNumber = random.randrange(0,100)
print("Random number has been generated")

count = 0
guessed = False

while guessed==False:

    count +=1

    userInput = int(input("Your guess please: "))

    if userInput==randomNumber:
        guessed = True
        print("Well done!")
        print("You tried " + str(count) + " times.")

    elif userInput>100:
        print("Our guess range is between 0 and 100, please try a bit lower")

    elif userInput<0:
        print("Our guess range is between 0 and 100, please try a bit higher")

    elif userInput>randomNumber:
        print("Try one more time, a bit lower")

    elif userInput < randomNumber:
        print("Try one more time, a bit higher")


