def start_game():
    print("Welcome to the game Hangman")
    print(r"""      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/ """)
    max_tries: int = 6
    print(max_tries)
    num_of_tries: int = 0
    while True :
        try:
            location_of_word: int = int(input("Please enter the number of the word (in the file) that you would like to try to guess "))
            break
        except ValueError:
            print("Input is not a number. Try again")
    while True:
        try:
            path_to_words: str = input("Please enter the path to the words file (an option is :words.txt ) ")
            secret_word: str = choose_word(path_to_words, location_of_word)[1]
            break
        except FileNotFoundError :
            print("I couldn't find the file ):  Please try again")

    print("Great lets start playing!!! \n \n")

    old_letters_guessed: list = []
    print_hangman(num_of_tries)
    hidden_word: str = "_ " * len(secret_word)
    print(hidden_word)

    while not check_win(secret_word, old_letters_guessed, num_of_tries):
        guess = input("Please guess a letter ")
        if check_valid_input(guess, old_letters_guessed):
            old_letters_guessed += guess
            if check_guess(guess,secret_word):
                print("Well done! I am proud of you !")
            else:
                print("Better luck next time ): ")
                num_of_tries+=1
                print_hangman(num_of_tries)
        print(show_hidden_word(secret_word,old_letters_guessed))

    if num_of_tries==6:
        print(f"You have lost ): But always keep looking forward... The word was {secret_word}")
    else:
        print(f"Nice - YOU HAVE WON ! I couldn't have done a better job myself ! The word was indeed {secret_word}")

def check_valid_input(letter_guessed: str, old_letters_guessed: list):
    if not len(letter_guessed) > 1 and letter_guessed.isalpha() and letter_guessed not in old_letters_guessed:
        return True
    print("X")
    print(" -> ".join(old_letters_guessed))
    return False

def show_hidden_word(secret_word: str, old_letters_guessed: list):
    show_word: str = ''
    for letter in secret_word:
        if letter in old_letters_guessed or letter.lower() in old_letters_guessed:
            show_word += " " + letter
        else:
            show_word += " _ "
    return show_word

def check_guess(guess:str,secret_words : str):
    if guess in secret_words.lower():
        return True
    return False

def check_win(secret_word: str, old_letters_guessed: list ,num_of_tries:int):
    count_letters_left: int = len(secret_word)
    for letter in secret_word.lower():
        if letter in old_letters_guessed:
            count_letters_left -= 1
    return count_letters_left == 0 or num_of_tries==6

def print_hangman(num_of_tries):
    hangman_photos = {0: "x-------x",
                     1: """    x-------x
     |
     |
     |
     |
     |""",
                     2: """    x-------x
     |       |
     |       0
     |
     |
     |""",
                     3: """    x-------x
     |       |
     |       0
     |       |
     |
     |""",
                     4: r"""     x-------x
     |       |
     |       0
     |      /|\
     |
     |""",
                     5: r"""    x-------x
     |       |
     |       0
     |      /|\
     |      /
     |""",
                     6: r"""   x-------x
     |       |
     |       0
     |      /|\
     |      / \
     |"""}
    print(hangman_photos[num_of_tries])

def choose_word(file_path:str, index:int):
    with open(file_path, 'r') as words_file:
        words:tuple = words_file.read().split(" ")
        no_duplicates_words:set =set(words)
        index = (index-1)% len(words)
        return len(no_duplicates_words),words[index]

def main():
    while True:
        start_game()
        if not input("Would you like to play again? ") == "yes":
            break

if __name__ == "__main__":
    main()