"""
Author: Vahid Keshmiri
Email: V.Keshmiry@Gmail.com

This module implements a finite state machine (FSM) for a simple chatbot. The chatbot goes through 
a sequence of states based on user inputs, demonstrating how a finite state machine can be used 
to manage chatbot conversations.
"""

from enum import Enum, auto

class State(Enum):
    """
    Enumeration for the states in the chatbot FSM.
    """
    START = auto()
    ASK_NAME = auto()
    ASK_AGE = auto()
    END = auto()

class Chatbot:
    """
    A simple chatbot implemented using a finite state machine.
    """

    def __init__(self):
        """
        Initializes the chatbot with the START state.
        """
        self.state = State.START

    def handle_message(self, message: str):
        """
        Handles a message and transitions between states.

        Parameters:
        message (str): The input message from the user.

        Returns:
        str: The response from the chatbot.
        """
        if self.state == State.START:
            return self._start()
        elif self.state == State.ASK_NAME:
            return self._ask_name(message)
        elif self.state == State.ASK_AGE:
            return self._ask_age(message)
        elif self.state == State.END:
            return self._end()

    def _start(self):
        """
        Handles the START state.

        Returns:
        str: The response asking for the user's name.
        """
        self.state = State.ASK_NAME
        return "Hi! What's your name?"

    def _ask_name(self, message: str):
        """
        Handles the ASK_NAME state.

        Parameters:
        message (str): The user's name.

        Returns:
        str: The response asking for the user's age.
        """
        self.user_name = message
        self.state = State.ASK_AGE
        return f"Nice to meet you, {self.user_name}. How old are you?"

    def _ask_age(self, message: str):
        """
        Handles the ASK_AGE state.

        Parameters:
        message (str): The user's age.

        Returns:
        str: The response indicating the end of the conversation.
        """
        self.user_age = message
        self.state = State.END
        return f"{self.user_age} is a great age to be! It was nice chatting with you!"

    def _end(self):
        """
        Handles the END state.

        Returns:
        str: The final goodbye message.
        """
        return "Goodbye!"

# Example usage
if __name__ == "__main__":
    chatbot = Chatbot()
    print(chatbot.handle_message(""))
    print(chatbot.handle_message("Alice"))
    print(chatbot.handle_message("25"))
