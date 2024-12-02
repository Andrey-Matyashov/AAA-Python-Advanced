import sys
from typing import Callable
from functools import wraps


def redirect_output(filepath: str) -> Callable:
    """
    A decorator that redirects the output of a function to a given file.

    :param filepath: A path to the file where the output should be redirected
    :return: A decorator that redirects the output of the decorated function
    """
    def decorator(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args, **kwargs):
            original_stdout = sys.stdout
            with open(filepath, 'w') as file:
                sys.stdout = file
                function(*args, **kwargs)
            sys.stdout = original_stdout
        return wrapper
    return decorator


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    calculate()
