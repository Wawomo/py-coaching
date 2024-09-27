#json
import json
#javascript object notation
myInfo = {
    "name" :"monica",
    "age" :60
}

# convert our dictionary into a json string using the dumps method
print(type(myInfo))
print(myInfo)
jsonString = json.dumps(myInfo, indent=2,sort_keys=True)
print(type(jsonString))
print(jsonString)
#dumps method id used to convert
#convert json string back to the python dictionary
converted = json.loads(jsonString)
print(type(converted))
print(converted['name'])