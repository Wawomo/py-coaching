import file13
#renaming imported modules eg. 
import file13 as myModule
#impoerting a single function from a module eg. 
from file13 import greeting, myInfo

print(file13.greeting('monica'))

name = file13.myInfo['name']
print(file13.greeting(name))

print(myModule.greeting ('mark'))

print(greeting('danny'))
print(myInfo)
