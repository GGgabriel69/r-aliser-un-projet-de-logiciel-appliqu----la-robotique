import json

x =  '{ "name":"Gabriel",  "age":18,  "isAlive":true }'


y = json.loads(x)

print(y["name"])
print(y["age"])
print(y["isAlive"])

z = json.dumps(x)

print(z)