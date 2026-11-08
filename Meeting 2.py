# Fundamentals
# Variable --> Data Structure like a box in memory we use to store different values of different Data Types
# To create a var we use name considering the rules of naming then use single equal operator --> =
# First the Declaration we name the variable then = to store a value and this is initialization and Assignment
var1 = 0

# NOTE : Difference between single = and double ==
comparing = (var1 == 1)

# To Know the result we use Function print()
print(var1)
print(comparing)

# To know the data type of the result or value we use Function type()
print(type(var1))
print(type(comparing))
"""
Resuts are: 
0
False
<class 'int'>
<class 'bool'>
"""

# Data Types --> str , int , float , boolean
# Take care strings in python class type is str not String
# Take care booleans in python class type is bool not boolean
print(type("Hello My Dear Students"))
print(type(True))
"""
Resuts are: 
<class 'str'>
<class 'bool'>
"""

# NOTE: no char type in python str of length 1

# NOTE: print() function has default new line take care of this
print("hello")
print("python")
"""
Resuts are: 
hello
python
"""

# NOTE: the third print is in new line not next to second bec the second print has by default at it's end a new line as if we say \n
print("hello",end=" ")
print("python")
print("python")
"""
Resuts are: 
hello python
python
"""

# NOTE: if u put \n at the end a newline empty will be created bec of \n of the default print as if its two \n --> \n\n
print("hello\n")
print("python")
"""
Resuts are: 
hello

python
"""