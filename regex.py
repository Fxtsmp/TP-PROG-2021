import re


def aircraft_id_code_validator(id_code):
    """ return True if the id_code of aircraft is rigth 
        en other case false
    

    Args:
        id_code (str): aricraft id code

    Returns:
        boolean: True is the id code follow the 
        standart rules in other case False
    """    
    pattern = re.compile(r'''L[QV]-[A-Z]+\d*''')
    return re.match(pattern, id_code) != None
