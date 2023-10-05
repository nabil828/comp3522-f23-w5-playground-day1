import json
person_dict = {"name": "Homer", "children": ["Bart", "Lisa","Maggie"],
"married": True, "fav_food": 'Donut' }

with open('person.json', 'w') as json_file:
  json_data = json.dumps(person_dict)
  json_file.write(json_data)