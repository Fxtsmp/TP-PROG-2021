from random import randrange
from os import system
from platform import system as sy
from copy import deepcopy


# funcion que limpia la consola
# segun el sistema operativo en
# el que este

def clear_screen():
    """clear the terminal according on the operating system
    """
    if sy() == "Windows":
        system("cls")
    else:
        system("clear")

# -------------------auxiliar function's-----------------------------


def number_integer_to_list(number_integer):
    """convert a integer number into a list

    Args:
        number_integer (int): a integer number

    Returns:
        list: a list with all digits of the number
    """
    return -1 if number_integer < 0 else list(str(number_integer))


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
    if not input_value.isdigit() and input_value == "":
        return -1
    else:
        return int(input_value)
# -------------------------------------------------------------------

# Recursion -> ejercicio 1
# put here the recursive approach

def sustitution_parx_1_imparx_2(list_of_digits):
    if len(list_of_digits) == 1:
        if int(list_of_digits[0]) % 2 == 0:
            list_of_digits[0] = "1"
        else:
            list_of_digits[0] = "2"
    else:
        if int(list_of_digits[0]) % 2 == 0:
            list_of_digits[0] = "1"
        else:
            list_of_digits[0] = "2"
        list_of_digits[1:] = sustitution_parx_1_imparx_2(list_of_digits[1:])
    return list_of_digits

# for the last
# Recursion -> ejercicio 2
# put here the recursive approach

def merge_all_list_into_one_list(list_of_list):
    pass

# Recursion -> ejercicio 3
# put here the recursive approach

def are_equals(list_of_int_1, list_of_int_2):
    """verified that the two list of ints are equals respect position and element

    Args:
        list_of_int_1 (int): a list of integer numbers
        list_of_int_2 (int): a list of integer numbers

    Returns:
        boolean: True if the list are equals else False
    """    
    if len(list_of_int_1) != len(list_of_int_2) or len(list_of_int_1) == 0 or len(list_of_int_2) == 0:
        return False
    elif len(list_of_int_1) == 1:
        return list_of_int_1[0] == list_of_int_2[0]
    else:
        return list_of_int_1[0] == list_of_int_2[0] and are_equals(list_of_int_1[1:], list_of_int_2[1:])

# Recursion -> ejercicio 4
# put here the recursive approach

def integer_division_by_sustract(dividend, divisor):
    if divisor == 0:
        return None
    elif divisor > dividend:
        return 0
    else:
        return integer_division_by_sustract(dividend-divisor, divisor) + 1
    
# for testing functions
def main():
    clear_screen()
    """ number_integer = input_with_default("enter a integer number ")
    print(list_to_number(sustitution_parx_1_imparx_2(
        number_integer_to_list(number_integer)))) """
    int1 = [1]  # [1,2,7,4,5]
    int2 = [1, 2, 3, 4, 5]
    print(are_equals(int1, int2))
    print(integer_division_by_sustract(int(input("dividend ")),int(input("divisor "))))

if __name__ == "__main__":
    main()
