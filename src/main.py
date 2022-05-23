import random

from numpy import number

correctNumber = random.randint(1, 100)
numberOfAttempts = 5
tries = 1

def main():
    global tries
    title()

    for tries in range(tries, numberOfAttempts + 1):
        print("\nTry {} of {}".format(tries, numberOfAttempts))
        try:
            number = chooseNumber()
        except ValueError as err:
            print("\nThat's not a value number. Try again...")
            continue
        
        if checkIfNumber(number):
            win = number == correctNumber
            higher = number < correctNumber
            lower = number > correctNumber

            if win:
                finalMessageWin(tries)
                break
            else:
                tries += 1
                finalMessageLose(higher, lower)
        else:
            break
    checkEndGame(tries)


def title():
    print("\nWelcome to the Guess Number game!!!\n")

def chooseNumber():
    number = int(input("Type a number between 1 and 100: "))
    return number

def checkIfNumber(number):
    return 1 <= number <= 100
    
def checkEndGame(tries):
    if tries == numberOfAttempts + 1:
        print("\nEND GAME!")
        print("\nThe number was {}".format(correctNumber))

def finalMessageWin(tries):
    print("\nThat's right, you found it!!!")
    if tries ==  1:
        print("It took you only 1 try to find it")
    else:
        print("It took you {} times to guess the right number".format(tries))

def finalMessageLose(higher, lower):
    print("\nOps... That's not the correct number.")
    if higher:
        print("The correct number is HIGHER!")
    elif lower:
        print("The correct number is LOWER!")


if __name__ == "__main__":
    main()