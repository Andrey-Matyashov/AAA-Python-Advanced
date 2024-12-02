import sys
import datetime

original_write = sys.stdout.write


def my_write(string_text: str) -> int:

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


if __name__ == '__main__':
    sys.stdout.write = my_write
    print('1, 2, 3')
