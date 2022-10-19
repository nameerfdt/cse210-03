from word import Word

class Puzzle:
    """An interactive handler for puzzle related elements for the
    Jumper game"""
    def __init__(self):
        """Initializes Puzzle with needed values and imports"""
        self._word = Word()
        self._secret_word = []
        self._incorrect_guesses = 0
        self._correct_guessed =[]
    
    def store_word(self):
        """Stores a word in self._secret_word for use
        with the compare function. Has a commented option for 
        dificulty selection if needed"""
        self._secret_word = self._word.get_word()
        for i in self._secret_word:
            self._correct_guessed.append("_")

        """self._secret_word = self._word.get_word(difficulty)"""

    def guess_compare(self, guess):
        """Compares guess to letters in word (list). If the letter
        is in the list is will replace the _ from the _correct_guessed variable
        otherwise it will check other letters through the rest of the word.
        
        If the letter is not present at all the function will increase
        incorrect_guesses by one."""
        current_digit = 0
        total_incorrect_checks = 0
        for letter in self._secret_word:
            if guess == letter:
                self._correct_guessed[current_digit] = letter
            else:
                total_incorrect_checks += 1
            current_digit += 1
        if total_incorrect_checks == len(self._secret_word):
            self._incorrect_guesses += 1
            
        
    
    def get_incorrect(self):
        """Returns Number Incorrect Guesses to a Director"""
        return self._incorrect_guesses
    def get_correct(self):
        """Returns List Containing correct guesses"""
        return self._correct_guessed
    

