#string formatting 
amount = 1000000
res = f'Your amount is {amount} Ugx'
print(res)
#inserting commas to integer values formatted 
res = f'Your amount is {amount:,} Ugx'
print(res)
#working with decimal values
res = f'Your amount is {amount:.2f} Ugx'
print(res)
#operations can be performed in side formatted strings
res = f'Your amount is {amount * 1.1} Ugx'
print(res)
#conditional statements can be performed inside the formatted string
res = f'Your amount {amount} is {'in range' if amount <= 1000000 else 'out of range'}'
print(res)

res = 'Your amount is {} Ugx'.format(amount)
print(res)

x = 5
y = 10
z = 20

res = 'x is {} and y is {} and z is {}'.format(x, y, z)
print(res)

#indexing formatted strings 
res = 'x is {0} and y is {1} and z is {2}'.format(x, y, z)
print(res)


"""
use pip to create a virtual environment 
activate the created environment 
install the packages of interest to the envronment 
import and use as required!

python -m venv venv
cd venv/Scripts 
activate
cd ../..
install packages that you need using pip 
pip install pyJWT
"""
