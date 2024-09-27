#introduction to python programming
#print()

    #numbers

    #integers
#print(3)
#print(-3)
#print(22234455)

    #floats
#print(45.0)
#print(34455.0)
#print(-346.0)
    #unary operators
        #negative
#print(-3)
        #positive
#print(+3)
#arithmetic operators
 #addition(+)
#print(1+3)
#print(10+5)
#print(100+200)




 #subtraction(-)
#print(45-5)
#print(100-50)
 #division(/)
#print(10//5)
 #multipulication(*)
#print(2*2)
#print(10*2)
 #exponentiation(**)
#print(3**2)

#print(3//2)
#print(round(3/2))
# COMPUND expressions
#print(1+2-1)
#print(1+2*2)
#print((1+2)*2)

#variables and assignment
#temperature = 50*2
#print("cenlus", temperature)

#print_quote = True
#if print_quote:
#   print("To error is human, to forgive is divine")
#else:
 #   pass
#print_quote = False      

#mile = 5280 * 13
#print(mile)

#miles = 13
#feet = miles * 5280
#print(str(miles)+ "miles equals" + str(feet) + "feet.") 

# write a python statement that cal and prints no of seconds in 7hrs 21min 37sec
#print((7* 60 + 21)* 60 + 37)

#hours = 7
#mins = 21
#seconds = 37

#total_seconds = (hours * 60 + mins) * 60 + seconds
#print(str(hours) + "hours" + str(mins) + "mimutes" + str(seconds) + "seconds" + "equals to" + str(total_seconds) + "seconds")

#function to cal the area of a triangle

#def area (half, base , height):
#   half(1/2) * base * height
#  return area


#print(len(my_set))
#sample_string = 'string'
#print(str(sample_string) + "ly")


def find_longest_word(words):
  """Finds the longest word in a list of words.

  Args:
    words: A list of words.

  Returns:
    A tuple containing the longest word and its length.
  """

  longest_word = ""
  longest_length = 0

  for word in words:
    if len(word) > longest_length:
      longest_word = word
      longest_length = len(word)

  return longest_word, longest_length

# Example usage:
words = ["apple", "banana", "cherry", "date"]
longest_word, length = find_longest_word(words)
print("Longest word:", longest_word)
print("Length:", length)
