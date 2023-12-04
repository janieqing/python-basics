# Python Basics Lesson
A lesson outline for Girls Who Code's free coding workshop for kids, teaching Python basics. Kids are using RepLit, an online IDE on their individual laptops.

### Python History
  * Python is a programming language that can be used to: build websites,  automate tasks, and more!
  * Python was created in 1991 in Holland, by a man named Guido van Rossum.
  *  Python is one of the most popular programming languages today!

### Python Types
There are many different data types that Python uses, but today we will be focusing on integer (number) data types and string (word) data types.
 * Integers are whole numbers, so no decimals or fractions.
 * Strings are words, letters, and characters. When using strings, you must have quotation marks ("") around your string, like how you must use quotation marks when
   you are writing to show what someone has said!

Examples of Integers:
```python
5
17
100
12358660964382304
```

Examples of Strings:
```python
"Happy holidays!"
"It is almost time for winter break."
"coding"
```

### Python Variables
  * variables are containers that can store values for later use
  * to set a variable, you type in the name of your new variable, an equal sign (=), and whatever you want your variable to represent <br>

  
Examples of Setting Variables:
```python 
x = 25
name = "Sally"
holiday = "Christmas"
```
### Python Print
  * In Python, the print() function outputs a specified message to the screen.
  * You must put quotation marks "" and parentheses () around whatever you want to print, unless you are directly printing a variable. <br>

Examples of Printing in Python:
```python
print("45")
print("Happy Hannukah!")
```

Examples of Printing with Variables
```python
person = "Santa Claus"
y = 13
print(person) 
print(y)
```
### Python Basic Math
 * You can use Python to conduct some basic math calculations.
 * Use + for addition
 * Use - for subtraction
 * Use / for divison
 * Use * for multiplication

Examples of Basic Math in Python
```python
math1 = 4 + 15
print(math1)
math2 = 24 - 16
print(math2)
math3 = 5 * 3
print(math3)
math4 = 16/4
print(math4)
```

Examples of Basic Math in Python with Variables
```python
a = 4
b = 2
add = a + b
sub = a - b
mult = a * b
divide = a / b
```
### Python If-Else Statements
 * If-statements are used to make decisions.
 * I.e. (if this.... then that.)
 * It is used to decide whether a certain statement or block of statements will be executed or not.
 * You must indent after your if statement.
 * Else runs if your statement is NOT true.
 * Equals: a == b
 * Not Equals: a != b
 * Less than: a < b
 * Greater than: a > b
 * Less than or equal to: a <= b
 * Greater than or equal to: a >= b

Basic Set-Up of an If-Else Statement:
```python
if condition:
   # Statements to execute if
   # condition is true
else:
   # Statement to execute else
   # condition is false
```
Examples of If-Else Statements:
```python
a = 33
b = 200
if b > a:
  print("b is greater than a")
else:
  print("b is less than a")

name = "Octo"
if name == "Tom":
   print("name is Tom, incorrect.")
else:
   print("name is not Tom.)
```
### Python Input
 * the input() function allows the user to input information to the program
 * set your input as a variable
 * the default input will be a string, however, integer inputs are also possible by using int(input())

Examples of String Input:
```python
x = input("Enter your name: ")
print(x)

password = input("What is the password? ")
print(password)
```

Examples of Integer Input:
```python
number = int(input("Enter a number: ")
print(number)
```


