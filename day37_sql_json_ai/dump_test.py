import json

data = {'name' : 'elice','age' : 25}
print(data)
print(type(data))

with open("./day37_sql_json_ai/dump_test.json", "w") as f:
    json.dump(data, f)
