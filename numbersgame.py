import random


def game():
    # generate a random number from 1 to 10
    secret_num = random.randint(1, 10)
    guesses = []
    while len(guesses) < 5:
        try:
            # get a number guess from a player
            guess = int(input("Get a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number".format(guess))
        else:
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("My number is higher than {}".format(guess))
            else:
                print("My number is lower than {}".format(guess))
            guesses.append(guess)
    else:
        print("You didn't get it, my number was".format(secret_num))
    play_again = input("do you want to play again? Y/n")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")