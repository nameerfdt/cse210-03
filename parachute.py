class Parachute:
    """A man and his parachute

    The responsibility of Parachute is to display the state of the Parachute based on a number of wrong guesses

    Attributes:
         _parachute_state (list): A list representing the Parachute
    """

    def __init__(self):
        """Constructs a new instance of Parachute with the parachute state

        Args:
            self (Parachute): An instance of Parachute.
        """
        self._parachute_state = [
            " ___",
            "/___\\",
            "\\   /",
            " \\ /",
            "  O",
            " /|\\",
            " / \\",
            "",
            "^^^^^"]

    def display(self, wrong_guesses):
        """Displays the parachute based on the number of wrong guesses

               Args:
                   self (Parachute): An instance of Deck.
                   wrong_guesses (int): The number of wrong_guesses. A number over 4 will be changed into 4.
               """
        if wrong_guesses > 4:
            wrong_guesses = 4
            self._parachute_state[4] = "  x"
        else:
            self._parachute_state[4] = "  O"
        return "\n".join(self._parachute_state[wrong_guesses:])


if __name__ == '__main__':
    parachute = Parachute()
    parachute_display = parachute.display(1)
    print(parachute_display)
