#!/usr/bin/python3
import json
import cmd

"""
    Creattion a simple flow of serialization/deserialization:
    Instance <-> Dictionary <-> JSON string <-> file
"""


class Person:
    """
        This is a base class for Person
        Args:
            name: (string)
            age: (integer)
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Create an instance of Person
person = Person("Wafa", "30")

# Serialize instance to a ditionary
person_dic = {
        "name": person.name,
        "age": person.age
}

print(person_dic)


# Serialize the dictionary to a Json string
json_string = json.dumps(person_dic)
print(json_string)

# Deserialize the Json to a dictionary:
recovered_dic = json.loads(json_string)
print(recovered_dic)


# serilize the diction to a json file
with open("person.json", "w") as json_file:
    json.dump(recovered_dic, json_file)

# Deselization: read the diction from JSon file
with open("person.json", "r") as json_file:
    loaded_dic = json.load(json_file)
print(loaded_dic)
