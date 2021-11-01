import xml.etree.cElementTree as et
from utils import clear_screen


def xml_list_availables_stations(root):
    # listar estaciones disponibles
    if root == None:
        print("no information available - problem with read information from file")
        return []
    print("Listing availables stations")
    list_of_stations = []
    for station in root.findall("station"):
        list_of_stations.append(station)
        print(station.get("name"))
    return list_of_stations


def xml_showing_station_information(station, station_name):
    print(
        f'''Quantity of sensors in station {station.get("name").capitalize()}: {station.find("number_of_sensors").text}''')
    for sensor in station[2:]:
        if sensor.get("active") == "True":
            print(
                f'''{sensor.tag.capitalize()}\t:\t{sensor[0].text}{sensor[1].text}''')


def xml_select_station(list_of_stations, position):
    if len(list_of_stations) < position or list_of_stations == []:
        return None
    else:
        return list_of_stations[position]

def xml_get_data_from_file(file):
    tree_ff = et.parse('./' + file)
    root_ff = tree_ff.getroot()
    return et.fromstring(et.tostring(root_ff, encoding='utf8').decode('utf8'))    


'''
    Algoritmo:
    Listo todas las estaciones disponibles(nombres)
    Pido nombre de estacion
    Si el nombre esta en la lista:
        mostrar(
            Cantidad de sensores de la estación nombre estacion: cantidad de sensores
            muestro todos los sensores disponibles, sensores que active="true" 
            Temperatura: medida unidad
            Humedad: medida unidad
            Velocidad Viento: medida unidad
        )
    Sino 
'''
