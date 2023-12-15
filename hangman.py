import random

def choose_word():
    words = ["python", "hangman", "programming", "code", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    chosen_word = choose_word()
    guessed_letters = []
    attempts = 3

    print("Welcome to Hangman")
    
    while attempts > 0:
        print("Attempts left:", attempts)
        current_display = display_word(chosen_word, guessed_letters)
        print("Current word:", current_display)

        guess = input("Enter a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guess that")
            elif guess in chosen_word:
                print("very good you guess")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                attempts -= 1
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")

        if "_" not in display_word(chosen_word, guessed_letters):
            print("Congratulations! You guessed the word:", chosen_word)
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", chosen_word)

hangman()