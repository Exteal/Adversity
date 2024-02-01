
import json
from recommandation import Recommandation, RecommandationWidget


file_name = "recommandations"
txt_path = file_name + ".txt"
json_path = file_name + ".json"

def recommand():
    return read_from_json_file(json_path)

def test_recommandation():
    return [RecommandationWidget("Recommandation 1", "Read", 1000), RecommandationWidget("Recommandation 2", "Write", 2000),
             RecommandationWidget("Recommandation 3", "Read", 3000), RecommandationWidget("Recommandation 4", "Lorem ipsum dolor sit amet.",0)]

def read_from_txt_file(path):
    recommandation_list = []
    with open(path, "r") as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            header, body = line.split(":")
            recommandation_list.append(Recommandation(header, body))
    return recommandation_list


def parse_recommandation_widget(recommandation):
    return RecommandationWidget(recommandation["header"], recommandation["body"], recommandation["timeout_seconds"] * 1000)

def read_from_json_file(path):
    recommandation_list = []
    with open(path, "r") as file:
        data = json.loads(file.read())

        for recommandation in data:
            recommandation_list.append(parse_recommandation_widget(recommandation))
    return recommandation_list

def input_recommandation():
    return []