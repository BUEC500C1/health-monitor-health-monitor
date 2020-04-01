import array
import random
import json

def read_file():
    file = open("oxygen_data.txt", "r")
    data = array.array('i', [])
    for line in file:
        data.append(int(line))
    return data

def get_oxygen():
    data = read_file()
    data_set = {"name": "oxygen", "values": []}
    json_dump = json.dumps(data_set)
    json_object = json.loads(json_dump)
    json_object["values"].append(data[random.randint(0, 99)])
    return json_object

if __name__ == '__main__':
    print(get_oxygen())
