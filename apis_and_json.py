import json

# Load JSON: json_data
with open("example.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])


print(json_data["GlossEntry"][0])