import json
import pprint
from datetime import datetime

with open('edi-210.json', 'r') as read_file:
    data = json.load(read_file)

with open('mastery-json_' + str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '.json', 'w') as write_file:
    json.dump(data, write_file, indent=2)
    json_string = json.dumps(data, indent=2, sort_keys = False)
    print(json_string)
