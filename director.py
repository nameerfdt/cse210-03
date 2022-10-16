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

    def welcome(self):
        #variable for welcome message
        welcome = ("\n         »»————-★————-««"
                 "\n ╔═════════════════════════════╗"
                 "\n∞╢ Welcome to the Jumper game  ╟∞"
                 "\n ╚═════════════════════════════╝"
                 "\n  ✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩"
                 "\n"
                 "\nDesigned by: Alex, Joshua, Tracy, and Mark")
        #call the terminal_service class write_text method to display welcome to terminal         
        self._terminal_service.write_text(welcome)

    def display_rules(self):
        #variable to display game rules
        rules = ("\nGame Rules:"
                 "\n"
                 "\nThe puzzle is a secret word randomly chosen from a list."
                 "\nThe player guesses a letter in the puzzle."
                 "\nIf the guess in correct, the letter is revealed."
                 "\nIf the guess is incorrect, a line is cut on the player's parachute."
                 "\nIf the puzzle is solved the game is over."
                 "\nIf the player has no more parchute the game is over."
                 "\nPlayer can choose if they want to play again.")
        #call the terminal_service class write_text method to display rules to terminal
        self._terminal_service.write_text(rules)

    def start_game(self):
        '''Starts the jumper game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        '''
        #main game loop until number of guesses is exceeded
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            self._play_again = False

    def _get_inputs(self):
        '''Get the player's input and returns it to puzzle
        to compare with the secret word.
        
        Args:
            self(Director): An instance of Director
        '''
        #reads player input from terminal
        guess = self._terminal.read_text("\nGuess a letter: ")
        self._puzzle.guess_compare(guess)
        
    def _do_updates(self):
        '''Keeps track of player guesses

        Args:
            self (Director): An instance of Director
        '''
        #self.get_incorrect returns self._incorrect_guesses to director
        #self.get_correct returns self._correct_guessed to director
        self._puzzle.get_incorrect(self._puzzle)
        self._puzzle.get_correct(self._puzzle)

    def _do_outputs(self):
        '''Shows parachute status
        
        Args:
            self (Director): An instance of Director
        '''   
        #set local variable equal to display parachute from Parachute   
        display_parachute = self._parachute.display(wrong_guesses) 
        #output parachute to the terminal
        self._terminal.write_text(display_parachute)
        #if puzzle incorret guesses is greater than 4 player loses
        if self._puzzle.incorrect_guesses > 4:
            #end loop for is_playing if incorrect guesses greater than 4
            self._is_playing = False
            play_again = self.terminal.read_text("Your lifeline is gone." 
                "Do you want to play again? (y or n): ")
            if play_again.lower() == "n":
                self._terminal.write_text("\nThanks for playing! Better luck next time!")
            else:
                self.play_again = True