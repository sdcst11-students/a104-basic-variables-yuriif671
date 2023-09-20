## SDSS Computing Studies Python Assignment
### Assignment #2 Basic Variables and Data Types (Total Marks 6)

Objectives:
* To store values in basic variables
* To retrieve basic variable values
* To display the contents of a variable using print()

In this lesson you will learn the basics of working with variables. Variables are extremely important in code, as they allow programs to be reusable for different applications.  For example, we might have a simple piece of code that adds 2 numbers together.  It would not be very effective for the code to only work for 1 + 1.  Instead, we want to be able to add any number to any other number.  In this case, we might use x + y where x and y are 2 variables representing the 2 numbers.

**Variable naming**:
* Variable names can be very short (a or b) or descriptive (EnglishGrade). Descriptive names are usually better as it makes understanding your code easier.
* Variable names must start with the "\_"underscore or with a letter, they may NOT start with a number
* Variable names can only contain alphanumeric symbols (A-Z,a-z,0-9) or the \_underscore
* Variable names are case sensitive

**How to assign values to variables:**
* variable = assigned value
* The variable always goes on the left.
* The = sign is an assignment operator.
* The right side can be a single value, string (word) or an expression that is to be evaluated before being assigned to your variable
  
  example:
 ``` 
  x = 10
  y = "Hello world"
  z = 2.4
  
  a = 10 + 3
  b = a / 2
```
**More Notes about Variables**
* If you assign a value to a variable more than once, the first value will be over written and will be gone forever (see file example3.py)

**Data Types**:
There are 3 basic data types in programming:\
int   : Integer values.  These are numbers that do not contain decimals. They may be positive or negative\
float : Floating Point values. These are numbers that do contain decimals\
str   : String.  This is a reference to a collection of symbols.  We may think of them as words, but they may contain alphanumeric characters.  Strings are contained within "double quotation marks" or 'single quotation marks'.\

Note that "10" is not the same as 10.  One is a string using symbols and the other refers to a numerical value.\


### 3 Tasks

##### Task 1
(2 points)\
Open the file assignment1.py\
Create 2 variables named x and y.  Assign a value of 10 to x and a value of 2.4 to y\
Output is not necessary.  The contents of the variables will be checked from within the program.\

#### Task 2
(2 points)\
Create a file called assignment2.py\
Create variables fname and lname\
Assign the string "Mr" to fname and the string "Yang" to lname\
Output is not necessary.  The contents of the variables will be checked from within the program.\

#### Task 3
(2 points)\
Create a file called assignment3.py\
Create variables value1 and value2\
Assign the numerical value of 10 to value1 and the string "10" to value2\
Output is not necessary.  The contents of the variables will be checked from within the program.\
