import json

json_string = '{"name": "Alice", "age": 30, "is_member": true}'
data = json.loads(json_string)

print(data["name"])
print(type(data))
user_profile = {"id": 101, "roles": ["admin", "user"]}
json_output = json.dumps(user_profile, indent=4) 

print(json_output)