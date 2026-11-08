import json

# --- JSON String to Python Object (Parsing / Deserializing) ---
json_string = '{"name": "Alice", "age": 30, "is_member": true}'
data = json.loads(json_string)

print(data["name"])      # Output: Alice
print(type(data))        # Output: <class 'dict'>

# --- Python Object to JSON String (Serializing) ---
user_profile = {"id": 101, "roles": ["admin", "user"]}
json_output = json.dumps(user_profile, indent=4) 

print(json_output)
# Output:
# {
#     "id": 101,
#     "roles": [
#         "admin",
#         "user"
#     ]
# }
