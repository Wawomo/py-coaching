import logging
logging.basicConfig(filename='log.txt', filemode='a', level=0)

#exception handling
"""
try:
    doing something
except: 
    handle the error
"""

try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    res = x / y
except ZeroDivisionError as e:
    #runs if the try block generates an exception
    logging.error(f'Error: {e}')
else:
    #runs if the block is successfull
    logging.info(f'The division of {x} and {y} is {res}')
    #print(f'The division of {x} and {y} is {res}')

finally:
    #runs regardless o ftry generating exception or not
    name = "david hope"
    print(name)
    print('I always no matter what!!!')

#raising exceptions 
x = 5

print(type(x))

#my program expects x to be a numerical value
if not type(x) is int:
    logging.critical('Expected Value For X is to be an Integer!')
    raise TypeError('Expected Value For X is to be an Integer!')


logging.info()
logging.debug()
logging.critical()
logging.exception()