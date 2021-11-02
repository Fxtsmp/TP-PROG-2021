import re
from typing import Pattern


def aircraft_id_code_validator(id_code):
    """ return True if the id_code of aircraft is rigth 
        en other case false
    

    Args:
        id_code (str): aricraft id code

    Returns:
        boolean: True is the id code follow the 
        standart rules in other case False
    """    
    
    """ re.compile(r'''L[QV]-[A-Z]+\d*''') """
    pattern = re.compile(r'''(L[QV]{1}-[A-Z]{3}|L[QV]{1}-[XS]{1,2}\d{3})''') 
    return re.match(pattern, id_code) != None

def number_below_1900(number):
    """validate if a number(str) is str < 1900

    Args:
        number (str): a natural number 

    Returns:
        bool: true if the number is < 1900 in other case False
    """    
    pattern = re.compile(r'''\b[0|1]?[0-8]?\d?\d\b''')
    return re.match(pattern, number) != None
