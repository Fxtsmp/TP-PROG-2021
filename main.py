from utils import clear_screen, input_with_default
from recursion import sustitution, are_equals, merge_all_list_into_one_list, integer_division_by_sustract


def main():
    clear_screen()
    # for testing, for now
    number_integer = input_with_default("enter a integer number ")
    print(sustitution(number_integer))
    int1 = [1]  # [1,2,7,4,5]
    int2 = [1, 2, 3, 4, 5]
    list_of_list = [[1,2,3],[4,5],[6,7]]
    list_of_list_2 = [['hola','como'],['va'],['todo']]
    print(merge_all_list_into_one_list(list_of_list))
    print(merge_all_list_into_one_list(list_of_list_2))
    print(are_equals(int1, int2))
    print(integer_division_by_sustract(
        int(input("dividend ")), int(input("divisor "))))


if __name__ == "__main__":
    main()
