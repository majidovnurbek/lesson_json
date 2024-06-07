# import json
# import requests
#
# url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(url)
# for posts in response.json():
#     with open("data.json", "w") as file_json:
#         json.dump(posts, file_json)

import json
import requests

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)
for user in response.json():
    with open("users.json", "w") as file_json:
        json.dump(user, file_json,indent=3)