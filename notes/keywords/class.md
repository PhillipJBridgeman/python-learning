# class
The `class` keyword is used for defining [classes](../classes.md) in Python.

## Syntax
```py
class ClassName:
  # Class body
```

The name of the class should be in CamelCase. The indented class body contains definitions for any attributes or methods. Class definitions cannot be empty, so the pass statement can be used as a placeholder to avoid errors.

```py
class ClassName:
  pass
```

## Example:
The following example is a small Python class made with the `class` keyword:

```py
class Student:
  def __init__(self, name, major):
    self.name = name
    self.major = major

code_ninja = Student("Code Ninja", "Computer Science")

print(f"Student name: {code_ninja.name}")
print(f"Major: {code_ninja.major}")
```

## Output
```bash
Student name: Code Ninja
Major: Computer Science
```