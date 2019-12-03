# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.append(y[0])
x.append(y[1])
x.append(y[2])
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
x.remove(9)
x.remove(10)
x.append(y[1])
x.append(y[2])
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5,99)
print(x)

# Print the length of list x
# YOUR CODE HERE 
print(len(x))
# Print all the values in x multiplied by 1000
# YOUR CODE HERE
i=0
while i <= len(x)-1:
    print (x[i]*1000)
    i+= 1

