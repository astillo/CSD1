"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = 33

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("This is %3d, the other one: %3d2, the last one:" % (x,y), "this is z: {}".format(z))
# Use the 'format' string method to print the same thing
print("this is {one}, this is: {two}, this is three{three}".format(one=x,two=y,three=z))
# Finally, print the same thing using an f-string
f'Results of the xyz are {x}, {y}, {z}'
