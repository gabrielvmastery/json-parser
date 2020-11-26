import json
import pprint

with open("edi-210.json", "r") as read_file:
    data = json.load(read_file)

with open("output_file3.json", "w") as write_file:
    json.dump(data, write_file)
    json_string = json.dumps(data, indent=2, sort_keys = False)
    print(json_string)
