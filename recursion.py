from utils import list_to_number, number_integer_to_list


# Recursion -> ejercicio 1
# put here the recursive approach

def sustitution_parx_1_imparx_2(list_of_digits):
    if list_of_digits == [] or not isinstance(list_of_digits, list):
        return ["0"]
    elif len(list_of_digits) == 1:
        list_of_digits[0] = "1" if int(list_of_digits[0]) % 2 == 0 else "2"
    else:
        list_of_digits[0] = "1" if int(list_of_digits[0]) % 2 == 0 else "2"
        list_of_digits[1:] = sustitution_parx_1_imparx_2(list_of_digits[1:])
    return list_of_digits


def sustitution(integer_number):
    return list_to_number(
        sustitution_parx_1_imparx_2(
            number_integer_to_list(integer_number)
        )
    )

# for the last
# Recursion -> ejercicio 2
# put here the recursive approach
'''

'''

def merge_all_list_into_one_list(list_of_list):
    """merge a list of list of elements into a only one list

    Args:
        list_of_list (list): list of list of any elements

    Returns:
        list: a list with all elements of the list contained inside the original list
    """    
    if len(list_of_list)==1:
        return list_of_list[0]
    else:
        return list_of_list[0] + merge_all_list_into_one_list(list_of_list[1:])


# Recursion -> ejercicio 3
# put here the recursive approach
'''
    Si las listas tienen difenrentes tamaño o alguna es nula no son iguales
    
    Sino    Si el tamaño de alguna de la lista es 1(en este caso ambas van a tener tamaño 1)
            retorno la igualdad entre los elementos de ambas listas
            
    Sino    Son iguales si el primer elemento de cada lista es el mismo, y los elementos de cada
            lista es el mismo en la sub lista que resulta de quitar el primer elemento de las
            mismas
'''


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
'''
    Si el divisor es 0 no se puede realizar la division
    
    Sino Si el divisor es mayor que el dividend entonces retorno 0
    
    Sino la division entera es la division entera de dividend - divisor
'''


def integer_division_by_sustract(dividend, divisor):
    """integer division using only substract

    Args:
        dividend (int): integer nummber
        divisor (int): integer number

    Returns:
        int: the result of integer division of dividend and divisor
    """
    if divisor == 0:
        return None
    elif divisor > dividend:
        return 0
    else:
        return integer_division_by_sustract(dividend-divisor, divisor) + 1


