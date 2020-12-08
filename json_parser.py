import json
import pprint
from datetime import datetime

with open('edi-204.json', 'r') as read_file:
    data = json.load(read_file)

with open(str(datetime.now().strftime('%Y%m%d-%H%M%S')) + '-mastery' + '.json', 'w') as write_file:

    json_string = json.dumps(data, indent=2, separators=(',', ':'), sort_keys = False)
    print(json_string)

    json.dump(data, write_file, indent=2,separators=(',', ':'))
read_file.close()
write_file.close()

#whitespaces are removed after ':' with separators=(',', ':')
#brackets []{} show up on newlines after ':'
