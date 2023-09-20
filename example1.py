#!python3

""" 
Assigning values to variables:
'''
Before you run this program, make sure that you have created your 'launch.json' file in the Run and Debug section of the Activity Bar. Then, click on the space to the left of line 9 (The one with the title of this program).  You will see a red dot show up when you mouse over it.  If you click on the dot, it will turn to a brighter red.
This creates a "breakpoint" in the program, or a point where the program pauses when you run and debug.  When the program reaches this point, it will pause and wait for you to continue working through the program.  You will notice a panel at the top of the screen that has an option to step into the program.  Notice how you can see the variables displayed in the debug panel as you do so.  You should notice the values of your variables change as you pass each line.
"""
print("Example1.py")
x = 3
y = 3.0
'''
Note that the next line will evaluate the expression to the right of the = sign BEFORE it is stored into your variable
'''
z = 3 + 4
greeting = "Hello"

'''
Note that you can include the contents of a variable in a print statement. It doesn't matter what the contents of a variable are. Printing a variable doesn't change the value of the variable
'''
print(x)
print(y)
print(z)
print(greeting)

'''
Note that you can store variables into other variables!
'''
x = 3
m = x
print(m)

'''
If we want to combine variables with literal text output, you need to use formatted strings.
Note the inclusion of the f in front of the quotation marks.  We can then just include the 
variable in the {} where we would like to show the value of that variable
'''
x = 2.5
print(f"The value of x is {x}")
