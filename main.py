import json

# Sample data
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Write data to JSON file
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Read data from JSON file
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)

# Access loaded data
name = loaded_data['name']
age = loaded_data['age']
city = loaded_data['city']

# Display loaded data
print("Name:", name)
print("Age:", age)
print("City:", city)
