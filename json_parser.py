import json
import pprint
from datetime import datetime
#loadobj= {"president": {"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}}

with open('edi-210.json', 'r') as read_file:
    data = json.load(read_file)

with open(str(datetime.now().strftime('%Y%m%d-%H%M%S')) + '-mastery' + '.json', 'w') as write_file:

    json_string = json.dumps(data, indent=2, sort_keys = False)
    print(json_string)

    json.dump(data, write_file, indent=2)
read_file.close()
write_file.close()
