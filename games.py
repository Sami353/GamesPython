from hangman import *
from wordle import *

def main():
    menu = True
    while menu == True:
        print('''
        What game would you want to play?
        1. Hangman
        2. Wordle
        3. Tic-tac-toe
        X. Exit
        ''')

        user_input = input("Enter the number of the Game you would like to Play: ").upper()

        match user_input:
            case "1":
                hangman()
                back = input("Would you like to go back to the main page? (Y/N): ").upper()
                if back == "Y":
                    continue
                else:
                    break
            case "2":
                wordle()
                back = input("Would you like to go back to the main page? (Y/N): ").upper()
                if back == "Y":
                    continue
                else:
                    break
            case "3":
                print("Under Construction")
                back = input("Would you like to go back to the main page? (Y/N): ").upper()
                if back == "Y":
                    continue
                else:
                    break
            case "X":
                break
    print("\033c")      
    print("Thank You! Byee! See You Later!")

if __name__ == '__main__':
    main()