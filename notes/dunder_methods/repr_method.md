# __repr__()
The `__repr__()` dunder method returns the string representation of the object or class. This overwrites the built-in `repr()` function.

## Syntax
```py
class ClassName:
  def __repr__(self):
```

The `__repr__()` method accepts no parameters. `self` is an implicit reference to the instance of ClassName.

## Example
A class string representation can be seen by calling [`print()`](../built-in_functions/print.md) on the instance. In the following example, the `__repr__()` method is written to return a formatted string representation of the `Home` class (with the help of the [`.format()`](../built-in_functions/format.md) string function):
```py
class Home:
  def __init__(self, rooms, stories):
    self.rooms = rooms
    self.stories = stories

  def __repr__(self):
    return "Home with {} rooms and {} stories".format(self.rooms, self.stories)

home1 = Home(4, 2)
print(home1)

home2 = Home(5, 2)
print(home2)
```

## Output
```bash
Home with 4 rooms and 2 stories
Home with 5 rooms and 2 stories
```