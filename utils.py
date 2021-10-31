from os import system
from platform import system as sy


'''
    this module contain functions that help another funtions
'''


def clear_screen():
    """clear the terminal according on the operating system
    """
    if sy() == "Windows":
        system("cls")
    else:
        system("clear")


def number_integer_to_list(number_integer):
    """convert a integer number into a list

    Args:
        number_integer (int): a integer number

    Returns:
        list: a list with all digits of the number
    """
    return [] if number_integer < 0 else list(str(number_integer))


def list_to_number(list_of_digits):
    """convert a list of digits on a integer number

    Args:
        list_of_digits (list): a list of digits of str type

    Returns:
        int: a number integer compost of digits of the list
    """
    return int("".join(list_of_digits))


def input_with_default(message):
    """a fork of normal input with a default value if introduce a empty value

    Args:
        message (str): message to show for the user

    Returns:
        int: a integer number
    """
    input_value = input(message)
    if isinstance(message, str):
        return "-1"
    else:
        return int(input_value)
