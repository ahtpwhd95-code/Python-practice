import json
from pprint import pprint 

f= open('day37_sql_json_ai/test.txt','r')
content = f.read()
f.close()
print(content)


with open('day37_sql_json_ai/test.txt','r') as f:
    content = f.read()
    print(content)

with open('day37_sql_json_ai/target.json','r') as f:
    data = json.load(f)
    
pprint(data)
print(type(data))

print(data['employee']['skills'])
