age = 18
#conditional statements
if age >= 18 :
    print("you are an adult")
else: 
    print("you are a minor")
#loops
for number in range(1,6):
    print(number)
while True:
    user_input = input ("enter a number (or 'quit' to exit):")
    if user_input == "quit": 
        break
    else:
            try : 
                 number = int(user_input)
                 print(number* 2)
            except  ValueError:
                 print("invalid input. Please enter a number.")