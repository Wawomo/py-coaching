price = 60
txt = f"it is very {'expensive'if price > 50 else 'cheap'}"
print(txt)

fruits = "apples"
txt1 = f"i love {fruits.upper()}"
print(txt1)
#custom function
def my_convertor(x):
    return x* 0.12 
text = f"this is the new price {my_convertor(786)}"
print(text)