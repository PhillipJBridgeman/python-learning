# Casting
Casting, also known as type conversion, is a process that converts a variable’s data type into another data type. These conversions can be implicit (automatically interpreted) or explicit (using built-in functions).

## Implicit Type Conversion
The Python interpreter automatically performs type conversion on some operations without any user involvement.

Python avoids data loss by converting lower data types to higher data types. For example, an integer, 7, is converted to a float when added with another float, 2.2:

```py
y = 7 + 2.2
# Python automatically type casts y into float

print(y)
# Output: 9.2

print(type(y))
# Output: <class 'float'>
```

Since the expression above represents the sum of two float values, the data type of y is also a float.

## Explicit Type Conversion
Explicit type casting involves Python’s predefined functions that act as a constructor of another data type:

- The str() function takes an integer or float as an argument and converts it to a string.
- The int() function takes a string or float as an argument converts it to an integer.
- The float() function takes an integer or string as an argument and converts it to a float.

Common functions:
| Function | Description | Example |
| -------- | ----------- | ------- |
| str() | Converts to string | str(5) → '5' |
| int() | Converts to integer | int("42") → 42 |
| float() | Converts to float | float("3.14") → 3.14 |

## Operations on Different Types of Data
When operating on data, it is important to be mindful of the data types associated with it. The following code is a flawed attempt to print the square of a number specified by the user. When run, a TypeError will be thrown:
```py
num = float(input("Please enter a number: "))
print(num ** 2)
```
The [`input()` function](./functions/input.md) takes input from the user and stores it in a variable as a string. However, the ** operator takes two numbers and returns the first number to the power of the second. In order to make the code work, the input variable must be cast to a number type.