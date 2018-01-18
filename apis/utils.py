import json

def print_json(my_json):
    parsed = json.loads(my_json)
    print json.dumps(parsed, indent=4, sort_keys=True)
