import json

info = {"name": "leila", "age" : 19, "city" : "kampala", "hubbies":12},

data = json.dumps(info, indent=4)
#print(data)


with open("info.json","w") as file30:
    file30.write(data)
print("JSON created successful")
with open("info.json","r") as file30:
    dat = json.load(file30)
print(dat["name"]) 

#import json
#x= {"name":"deno","age":15,"city":"kampala"}

#y = json.dumps(x, indent=4)
#print(y)

#with open ("x.json","w") as f:
#    f.write(y)

#print("JSON created as successful")

#with open ("x.json","r") as f:
 #   data = json.load(f)
#print(data["name"])