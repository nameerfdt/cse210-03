# Jumper overview
___
Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.  One line of the parachute is elliminated for each wrong guess.  If the player guesses the secret word with less than 4 incorrect guesses they win.  If the player gets 4 incorrect guesses their parachute is elliminated and they loose.

## Getting Started
___

Make sure you have Python 3.10 or newer installed and running on your machine. Open a terminal and 
browse to the project's root folder. Start the program by running the following command.
```
__main__.py
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the dice folder and click the "run" button.

## Project Structure
___

### director  (Tracy)
- __init__
    - self._puzzle = Puzzle()
    - self._parachute = Parachute()
    - self._terminal = Terminal()
- start game
- sends welcome/rules to terminal.print
- self._do_updates
- self._get_inputs
- self._do_outputs
- while game not over 
- sends game results to terminal to print
- ask if player wants to play again

### puzzle (Joahua)
- __init__
    - self._word = Word()
    - self._secret_word = ""
    - self._incorrect_guesses = int
    - self._correct_guessed = []
- functions list
    - self.store_word calls word class and stores word self.secret_word
    - self.guess_compare compares guess to word and stores correct guesses in self._correct_guessed and
      stores incorrect guess count in self._incorrect_guesses
    - self.get_incorrect returns self._incorrect_guesses to director
    - self.get_correct returns self._correct_guessed to director
    
### word class (Mark)
- __init__
  - self._word_list
      - random list of words
- self.get_word
    - select random word from word_list and returns it as a list to puzzle

### parachute (Alex)
- __init__
    - self._parachute
- self.display
    - (self, wrong_guesses)
    - display parachute

### terminal
- terminal.print

## Required Technologies
---
* Python 3.10

## Authors
---
* Alex Dahl (alexdahl@byui.edu)
* Tracy Freeman (nameerfdt@byui.edu)
* Joshua Herman (her21095@byui.edu)
* Mark Perry (per19039@byui.edu)
