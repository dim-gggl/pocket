"""
This module contains the ClinkeyView class.
"""

from typing import Any, Callable


class ClinkeyView:
    """
    This class is used to display the messages to the user.
    """
    messages = {
        "greeting": "Welcome to Clinkey",
        "yes_no_input": "Yes/No ? (y/n) : ",
        "password_type": (
            "Which type of password do you want to generate ?"
        ),
        "password_type_choice": {
            "1": "Simple (Only letters)",
            "2": "Medium (Letters and numbers)",
            "3": "Strong (Letters, numbers and symbols)"
        },
        "password_length": (
            "How long do you want your password to be ?"
        ),
        "error": "Error : ",
        "success": "Success : ",
        "info": "Info : "
    }

    def display_greeting(self) -> None:
        """
        Display the greeting message.
        """
        print("\n" * 20)
        print(f"{'Welcome to Clinkey':^90}")
        print("\n" * 5)
        input("Press Enter to continue...")

    def header(self) -> None:
        """
        Display the header of the program.
        """
        print("\n" * 20)
        print(f"{'======[ \033[5m Clinkey \033[0m ]======':^90}")
        print("\n" * 5)

    def headed(self, func: Callable) -> Callable:
        """
        Decorator to display the header of the program.
        """
        def wrapper(*args, **kwargs) -> Any:
            """
            Wrapper function to display the header of the program.
            """
            self.header()
            return func(*args, **kwargs)
        return wrapper

    def _get_user_yes_no_input(self, message: str) -> str:
        """
        Get the user's yes/no input.
        """
        self.header()
        print(f"{message:^90}")
        return input(f"{'Yes/No ? (y/n) : ':^90}")

    def _get_user_123_choice(self, message: str, choice: list[str]) -> str:
        """
        Get the user's 1/2/3 choice.
        """
        self.header()
        print(f"{message:^90}")
        print(f"{f'1 - {choice[0]}':^90}")
        print(f"{f'2 - {choice[1]}':^90}")
        print(f"{f'3 - {choice[2]}':^90}")
        return input(f"{'1/2/3 ? : ':^90}")

    def _get_user_input(self, message: str) -> str:
        """
        Get the user's input.
        """
        self.header()
        print(f"{message:^90}")
        return input(f"{'Your choice : ':^90}")

    def get_user_password_type(self) -> str:
        """
        Get the user's password type.
        """
        return self._get_user_123_choice(
            self.messages["password_type"],
            self.messages["password_type_choice"]
        )

    def get_user_password_length(self) -> str:
        """
        Get the user's password length.
        """
        return self._get_user_input(
            self.messages["password_length"]
        )

    def display_password(self, password: str) -> None:
        """
        Display the password.
        """
        self.header()
        print(f"\n\033[92m{password}\033[0m")
        print("\n" * 5)

    def display_error(self, message: str) -> None:
        """
        Display the error message.
        """
        self.header()
        print(f"\n\033[91m{message}\033[0m")
        print("\n" * 5)

    def display_success(self, message: str) -> None:
        """
        Display the success message.
        """
        self.header()
        print(f"\n\033[92m{message}\033[0m")
        print("\n" * 5)

    def display_info(self, message: str) -> None:
        """
        Display the info message.
        """
        self.header()
        print(f"\n\033[94m{message}\033[0m")
        print("\n" * 5)
