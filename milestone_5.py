import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = self._choose_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))

    def _choose_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        guess_lower = guess.lower()

        if guess_lower in self.word.lower():
            print(f"Good guess! {guess} is in the word.")

            for i, letter in enumerate(self.word):
                if letter == guess_lower:
                    self.word_guessed[i] = guess_lower

            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

# For testing the play_game function
word_list_for_testing = ["Mango", "Pineapple", "Orange", "Apple", "Banana"]
play_game(word_list_for_testing)
