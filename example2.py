#!python3

'''
Types of Variables
There are 3 basic types of variables that we will start learning about:

int
Integer numbers (these are numbers with no decimal)

float
Numbers with a decimal

str
Sting Literals.  These are not numbers, but are actually collections of symbols

Note that what you might think are the same are not the same!
'''
x = 3
y = 3.0
z = '3'
a = 'three'

print(f"x {x} is a type: { type(x) }")
print(f"y {y} is a type: { type(y) }")
print(f"y {z} is a type: { type(z) }")
print(f"y {a} is a type: { type(a) }")
exit()
'''
Notice that all of these variables now appear to contain some variation of 3, but they are not all the same.  
x contains an integer value
y contains a float value
and z contains a string literal

x and y contain the same amount (exactly 3) but z contains a symbol that represents the number 3 but it doesn't equal 3.  It's like the contents of the variable a.  It contains the word 'three', but that's not really a value of 3

When you run a program with a debugger, you can identify what kind of data is being stored by whether it contains:
a decimal point (a float)
no decimal point (an int)
or single quotation marks (a str)

We will see later on that we can convert some data into different data types as long as they contain the right contents.
'''

'''
type()
This command can help a program determine the type of data that a variable contains.  This is sometimes useful in helping us validate data before we do calculations.  You couldn't multiply 2 variables that are not some kind of number type, for example.
This command requires that you enter the variable that you want to find the type of inside the brackets.
Note that the contents will not be displayed unless you print it, or store it in a variable and then print it.
'''

x = 3
type(x)
'''
Note that nothing appeared when line 51 or 52 was executed because it was not printed
'''
typeOfVariable = type(x)
'''
This is also not printed, but the value is stored into the variable called 'typeOfVariable' 
'''
print( type(x) )
print( typeOfVariable )
y = 3.0
print( type(y) )

z = '3'
print( type(z) )

a = 'three'
print( type(a) )
a = "three"