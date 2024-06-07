import json

person = {
    "Name": "Nurbek",
    "surname": "majidov",
    "email": "majiodv@gmail.com",
    "full_name": {
        "first_name": "Nurbek",
        "last_name": "Majidov",
    },
    "age": 16
}
# data = json.dumps(person)
# print(data)
with open("person.json", "w") as file_json:
    json.dump(person, file_json,indent=10)
# # with open("data_file.json", "r") as read_file:
# #     data = json.loads(read_file)

# print(type(data))