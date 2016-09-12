import json


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.loads(file.read())


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    data = load_data('/home/lamberk/python/devman/4_json/data.json')
    pretty_print_json(data)
