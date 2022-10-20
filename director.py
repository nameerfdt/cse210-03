from terminal import TerminalService
from puzzle import Puzzle
from parachute import Parachute

class Director:
    '''A person who directs the game.
    
    The responsibility of a Director is to control the game play.
    
    Attributes:
        puzzle (Puzzle): handles the secret word and guesses.
        parachute (Parachute):
        terminal (Terminal): For displaying the game info on the terminal.
     '''
    def __init__(self):
        '''Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        '''
        self._puzzle = Puzzle()
        self._parachute = Parachute()
        self._terminal_service = TerminalService()
        self._is_playing = True
        self._incorrect_guesses = 0
        self._correct_guesses = 0
        self._current_game = True
        self._game_won = False

    def start_game(self):
        '''Starts the jumper game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        '''
        #variable for welcome message
        welcome = ("\n         »»————-★————-««"
                 "\n ╔═════════════════════════════╗"
                 "\n∞╢ Welcome to the Jumper game  ╟∞"
                 "\n ╚═════════════════════════════╝"
                 "\n  ✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩"
                 "\n"
                 "\nDesigned by: Alex, Joshua, Tracy, and Mark"
                 "\n")

        #variable to display game rules
        rules = ("\nGame Rules:"
                 "\n"
                 "\nThe puzzle is a secret word randomly chosen from a list."
                 "\nThe player guesses a letter in the puzzle."
                 "\nIf the guess in correct, the letter is revealed."
                 "\nIf the guess is incorrect, a line is cut on the player's parachute."
                 "\nIf the puzzle is solved the game is over."
                 "\nIf the player has no more parchute the game is over."
                 "\nPlayer can choose if they want to play again."
                 "\n")

        #call the terminal_service class write_text method to display welcome and rules
        self._terminal_service.write_text(welcome)        
        self._terminal_service.write_text(rules)

        #main game loop until number of guesses is exceeded
        while self._is_playing:
            self._puzzle.store_word()
            while self._current_game:
                self._get_inputs()
                self._do_updates()
                self._do_outputs()


    def _get_inputs(self):
        '''Get the player's input and returns it to puzzle
        to compare with the secret word.
        
        Args:
            self(Director): An instance of Director
        '''
        #reads player input from terminal and sends to puzzle
        guess = self._terminal_service.read_text("\nGuess a letter (a-z): ")
        self._puzzle.guess_compare(guess)
        
    def _do_updates(self):
        '''Keeps track of player guesses

        Args:
            self (Director): An instance of Director
        '''
        #self.get_incorrect returns self._incorrect_guesses to director
        #self.get_correct returns self._correct_guessed to director
        self._correct_guesses = self._puzzle.get_correct()
        self._incorrect_guesses = self._puzzle.get_incorrect()
        

    def _do_outputs(self):
        '''Shows parachute status
        
        Args:
            self (Director): An instance of Director
        '''     
     
        #output parachute to the terminal
        self._terminal_service.write_text(" ".join(self._correct_guesses))
        self._terminal_service.write_text(self._parachute.display(self._incorret_guesses))
        
        if "_" not in self._correct_guesses:
            self._game_won = True

        #if puzzle incorret guesses is greater than 4 player loses
        if self._incorrect_guesses > 4:
            #end loop for is_playing if incorrect guesses greater than 4            
            self._current_game = False
            play_again = self.terminal_service.read_text("\nYour lifeline is gone. Do you want to play again? (y or n): ")
            if play_again.lower() == "n":
                self._is_playing = False
                self._terminal_service.write_text("\nThanks for playing! Better luck next time!")
        elif self._game_won:
            self._current_game = False
            play_again = self.terminal_service.read_text("\nCongrats! You won! Do you want to play again? (y or n): ")
            if play_again.lower() == "n":
                self._is_playing = False
                self._terminal_service.write_text("\nThanks for playing! It's been fun!")