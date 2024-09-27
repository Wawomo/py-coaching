import jwt
info = {
    'name':'david hope',
    'age':30,
    'gender':'male'
}
encoded = jwt.encode(info, "#256Dave!!", algorithm="HS256")
print(encoded)
decoded = jwt.decode(encoded, "#256Dave!!", algorithms=["HS256"])
print(decoded)
