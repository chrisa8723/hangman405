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

# For testing the modifications
hangman_game = Hangman(["Mango", "Pineapple", "Orange", "Apple", "Banana"])

# Test the check_guess method with a valid guess
hangman_game.check_guess("x")
print("Word guessed after 'x':", hangman_game.word_guessed)
print("Number of lives left:", hangman_game.num_lives)
