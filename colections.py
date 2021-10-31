#colections exercise
#explain map,reduce and filter functions...

Map_function= print("the map function applies an N function to a sequence of elements and returns a new list with the modifications,receives as argument a function N and a list")

Reduce_function=print("The reduce function allows us to reduce a list to a single iterable element, it receives a function N and a list as parameters.")

Filter_function=print("the filter function receives as arguments a list and a function N and allows us to check if the elements of the list meet a certain condition.returns an iterable with the checked items.")


#algorithm for number pi with n number of numbers...
#point Nº2..

from functools import reduce


def generate_ns(n_esimo):
    if n_esimo == 0:
        return [0]
    else:
        return generate_ns(n_esimo - 1) + [n_esimo]


def suscession_pi(n_esimo):
    """calculate the terms of a suscession that aproxima a pi number

    Args:
        n_esimo (int): number that represent until that term we must calculate

    Returns:
        [list]: a list with n_esimo terms
    """
    return list(map(lambda n: (4 * ((-1) ** n)) / (2 * n + 1), generate_ns(n_esimo)))


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


