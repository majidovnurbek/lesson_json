import json
a="hello world"
with open("data.json", "w") as file_json:
    json.dump(a, file_json)