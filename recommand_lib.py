
import json

file_name = "recommandations"
txt_path = file_name + ".txt"
json_path = file_name + ".json"

def recommand():
    return read_from_json_file(json_path)

def test_recommandation():
    return ["Recommandation 1", "Recommandation 2", "Recommandation 3", "Recommandation 4"]

def read_from_txt_file(path):
    recommandation_list = []
    with open(path, "r") as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            recommandation_list.append(line)
    return recommandation_list


def read_from_json_file(path):
    recommandation_list = []
    with open(path, "r") as file:
        data = json.loads(file.read())

        for name, desc in data.items():
            recommandation_list.append(name + " : " + desc)
    return recommandation_list

def input_recommandation():
    return []