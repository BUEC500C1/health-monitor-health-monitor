import array
import random
import json

def read_file():
    file = open("oxygen/oxygen_data.txt", "r")
    data = array.array('i', [])
    for line in file:
        data.append(int(line))
    return data

def get_oxygen():
    data = read_file()
    data_set = {"name": "oxygen", "values": data[random.randint(0, 99)]}
    return data_set

if __name__ == '__main__':
    print(get_oxygen())
