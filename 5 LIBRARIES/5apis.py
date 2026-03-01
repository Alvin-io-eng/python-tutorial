import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# API example
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(response.json()) # ensures the data am getting back is formated as json but still return a whole blob in a dictionary format(ugly)

import json
# now with import json it has pretty printing(more presentable & readable) 
print(json.dumps(response.json(), indent = 2)) 

o = response.json()

for result in o["results"]:
    print(result["trackName "])
