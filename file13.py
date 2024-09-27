#python scope - concists of local and global variable scopes
#local
name = 'isaac'
def greeting():
    name = 'mick'
    return f'{name} , good afternoon!'

print(name)
print(greeting())

def myFunc():
    global msg
    msg = 'interesting'

myFunc()
print(msg)  

#modules- more like a library python eg json module. dont use reserved key words
def greeting(name):
    return f'hallo{name}'

myInfo = { 
    "name" : "monica",
    "age" : 60
}


