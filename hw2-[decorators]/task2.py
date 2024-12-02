import sys
import datetime
from typing import Callable
from functools import wraps, partial


def my_write(string_text: str, original_write: Callable) -> int:
    """
    Writes the given string text to the standard output with a timestamp.

    If the string text is a newline character, it writes an empty string.
    Otherwise, it prepends the current date and time in the format
    "YYYY-MM-DD HH:MM:SS" to the string text before writing it.

    Args:
        string_text (str): The text to write to standard output.

    Returns:
        int: The number of characters written.
    """
    if string_text == '\n':
        return original_write('')

    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return original_write(f'[{current_date}]: {string_text}\n')


def timed_output(function: Callable) -> Callable:
    """
    A decorator that wraps a function and prints the current date and time before
    and after the function is called. The date and time are printed in the format
    "YYYY-MM-DD HH:MM:SS".

    The function is called with the same arguments as the original function.

    Args:
        function (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        original_write = sys.stdout.write

        sys.stdout.write = partial(my_write, original_write=original_write)
        function(*args, **kwargs)
        sys.stdout.write = original_write
    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print_greeting("Nikita")
