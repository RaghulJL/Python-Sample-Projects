#Importing necessary modules
import random
import time
attempt_list = []
#Scoreboard
def score_board():
    if len(attempt_list)<=0:
        print("There is currently no High Score. It\'s yours for taking!")
    else:
        print("Your High Score is {} attempts".format(min(attempt_list)))
#Start game
def start_game():
    random_number = int(random.randint(1,50))
    print("Welcome to the Game of Guesses, Traveller!")
    time.sleep(1)  #Delay of 1 sec
    player_name = input("Your kind name?: ")
    time.sleep(1)  #Delay of 1 sec
    wanna_play = input("Hi {}, do you want to play the Game? (Enter Yes/No): ".format(player_name))
    attempts = 0
    score_board()
    while wanna_play.lower()=="yes":
        try:
            time.sleep(1)  # Delay of 1 sec
            guess=int(input("Select a no. between 1 and 50: "))
            if int(guess)<1 or int(guess)>50:
                time.sleep(1)  # Delay of 1 sec
                raise ValueError("Please guess a no. within the range")
            if int(guess)==random_number:
                time.sleep(1)  # Delay of 1 sec
                print("Nice! You got it right!")
                attempts += 1
                attempt_list.append(attempts)
                time.sleep(1)  # Delay of 1 sec
                print("It took you {} attempts".format(attempts))
                time.sleep(1)  # Delay of 1 sec
                play_again=input("Would you like to play again? (Enter Yes/No): ")
                attempts = 0
                score_board()
                random_number=int(random.randint(1,50))
                if play_again.lower()=="no":
                    time.sleep(1)  # Delay of 1 sec
                    print("That\'s fine! Have a great day")
                    break
            elif (guess)>random_number:
                time.sleep(1)  # Delay of 1 sec
                print("Too high...Try to go lower")
                attempts += 1
            elif (guess)<random_number:
                time.sleep(1)  # Delay of 1 sec
                print("Too bad...You should go higher")
                attempts += 1
        except ValueError as err:
            time.sleep(1)  # Delay of 1 sec
            print("Oh no! that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("That\'s fine! Have a great day")
if __name__ == '__main__':
    start_game()