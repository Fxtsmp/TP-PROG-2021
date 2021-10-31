from functools import reduce

def generate_ns(n_esimo):
    """generate a n's values integers

    Args:
        n_esimo (int): the quantity of numbers

    Returns:
        list: list of integers that represent the position in the suscession
    """    
    if n_esimo == 0:
        return [0]
    else:
        return generate_ns(n_esimo-1) + [n_esimo]
    
def suscession_pi(n_esimo):
    """calculate the terms of a suscession that aproxima a pi number

    Args:
        n_esimo (int): number that represent until that term we must calculate

    Returns:
        [list]: a list with n_esimo terms
    """    
    return list(map(lambda n: (4*((-1)**n))/(2*n+1), generate_ns(n_esimo)))


def calculate_pi(n_esimo):
    """calculate the number pi by aproximation

    Args:
        n_esimo (int): a natural number >= 0 

    Returns:
        float: a float number that aproximate the real value of pi
    """
    if n_esimo < 0:
        return -1
    elif n_esimo == 0:
        return 4.0
    else:
        return reduce(lambda a, b: a + b, suscession_pi(n_esimo))
