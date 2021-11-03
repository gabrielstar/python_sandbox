# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json


# sample json

userJSON = '{"first_name":"John", "last_name" :"Doe","age":30}'

# parse to dict
user = json.loads(userJSON)
user["age"] = 33
print(user)  # this is python dictionary

# dict to string
car = {"make": "Ford", "year": 1970}  # dict
carJSON = json.dumps(car)
print(carJSON)  # in JSON format
