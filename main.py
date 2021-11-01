from utils import *
from recursion import *
from regex import *
from colections import *
from exchange_data import *


def main():
    clear_screen()
    # for testing
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
    print('''number_below_1900("1901")''', number_below_1900("1901"))
    print('''number_below_1900("1899")''', number_below_1900("1899"))
    print('''number_below_1900("1")''', number_below_1900("1"))
    print('''number_below_1900("2000")''', number_below_1900("2000"))
    print(
        f'''aircraft_id_code_validator("LQ-AWQ")\t=\t{"valida" if aircraft_id_code_validator("LQ-AWQ") else "invalida"}''')
    print(
        f'''aircraft_id_code_validator("LV-123")\t=\t{"valida" if aircraft_id_code_validator("LV-123") else "invalida"}''')
    print(
        f'''aircraft_id_code_validator("LV-XS123")\t=\t{"valida" if aircraft_id_code_validator("LV-XS123") else "invalida"}''')
    print(
        f'''aircraft_id_code_validator("LV-S123")\t=\t{"valida" if aircraft_id_code_validator("LV-S123") else "invalida"}''')
    print(
        f'''aircraft_id_code_validator("LV-XS")\t=\t{"valida" if aircraft_id_code_validator("LV-XS") else "invalida"}''')
    print(calculate_pi(900))

    input("press enter to show xml exchange information")
    clear_screen()
    
    root = xml_get_data_from_file("model.xml")
    st = " "
    list_of_stations = []
    
    while st.lower() not in "exit":
        clear_screen()
        list_of_stations = xml_list_availables_stations(root)
        st = input("enter the station to show information number o name: ").strip()
        if st.lower() == "x":
            break
        clear_screen()
        xml_showing_station_information(xml_select_station(list_of_stations,xml_get_position_for_station(st, list_of_stations)),st)
        st = input(
            "press enter to request new station information or [x] to e[x]it: ")
        if st == "":
            st = " "
    # ------------------ showing th s station with the most low battery average
    battery_information = []
    battery_information = xml_get_most_low_battery_station(list_of_stations)
    print(f"the battery with the most low voltage is the battery of station  {battery_information[0]} with {battery_information[1]} {battery_information[2]} average")


if __name__ == "__main__":
    main()
