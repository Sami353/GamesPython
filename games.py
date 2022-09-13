from hangman import *
from wordle import *

def main():
    print('''What game would you want to play?
    1. Hangman
    2. Wordle
    3. Tic-tac-toe
    X. Exit
    ''')
    user_input = input("Enter the number of the Game you would like to Play: ").upper()

    match user_input:
        case "1":
            hangman()
        case "2":
            wordle()
        case "3":
            print("Under Construction")
        case "X":
            print("Bye")
    
if __name__ == '__main__':
    main()