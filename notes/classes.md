# Classes
**Classes** are templates used to define the properties and methods of objects in code. They can describe the kinds of data that the class holds, and also how a programmer interacts with that data.

The usage of classes are a key element of [object-oriented programming (OOP)](./general_topics/oop.md) where “class instances” are created to implement design principles such as [inheritance](./general_topics/inheritance.md) and [encapsulation](./general_topics/encapulation.md).

## Creating a Class
In Python, classes are defined using the **class** keyword. The first letter of the name of the class is always capitalized. For instance, the first letter of the `Home` class in the below example, i.e., ‘H’, is capitalized: 
```py
class Home:
  # Class body starts here
```
**Note:** The example above would actually be invalid because class definitions cannot be empty. However, the pass statement can be used as a placeholder to avoid errors:
```py
class Home:
  pass
```
In the class body, the `self` keyword, followed by a period `.`, can be used to call its methods and access its variables, as shown in the `__init__()` [dunder method](./dunder_methods.md) below:
```py
class Home:
  def __init__(self, rooms, stories):
    # Setting instance variables
    self.rooms = rooms
    self.stories = stories
```
## Class Instances
Objects can be created or instantiated from classes. These objects are known as class instances and are created by setting a variable equal to the class name followed by parentheses `()`:
```py
my_home = Home()
```
Here, the instance name is my_home, which derives from the Home class. Calling this line implicitly calls the Home class’s `__init__()` method.

## Attributes
Class attributes are variables that are defined outside of all methods and have the same value for every instance of the class. They also can be accessed via the class name rather than the instance name. Setting the variable via the class name will change it for all instances.

**Note:** Setting it via an instance name will break the connection for that instance.

```py
class Bird:
  # Class attribute
  is_hungry = True

parakeet = Bird()
parrot = Bird()


print("Birds are hungry!")
print("Feeding birds...")

parakeet.is_hungry = False
parrot.is_hungry = False

print("Birds fed!")
```

This will output the following:

```bash
Birds are hungry!
Feeding birds...
Birds fed!
```

## Methods
Methods are [functions](./functions.md) defined as part of a class. The first parameter for any class method, including dunder methods, is the actual object calling the method, usually called self.

The following is a slight modification of the Bird class from the previous section:

```py
class Bird:
  # Class attribute
  is_hungry = True

  def feed_bird(self, food):
    if(self.is_hungry):
      self.is_hungry = False
      print(f"Feeding with {food}. Bird fed!")
    else:
      print("Bird already ate.")

sparrow = Bird()

sparrow.feed_bird('seeds')
sparrow.feed_bird('oats')
```

A `feed_bird()` method is defined in the Bird class body, accepting a food parameter. Inside, an `if..else` [conditional](./conditionals.md) prints a different message depending on whether or not the `is_hungry` attribute is true. The following will be printed based on the example:

```bash
Feeding with seeds. Bird fed!
Bird already ate.\
```

## Static Methods
It is also possible to create a method that only applies to the class itself, not instances of the class. These can be distinguished with @classmethod and `@staticmethod`:
```py
class Home:
  name="Code Ninja"
  rooms = 4
  stories = 2

  @staticmethod
  def is_on_market(home):
    if(home.name == ""):
      return True
    else:
      return False

  @classmethod
  def paint_wall(self, color):
    return f"Painting wall with the color {color}."

home = Home()

print(Home.is_on_market(home))
# Output: False
```

## Example
The following example demonstrates an `Employee` class defined in a file called `employee.py`:

```py
# employee.py
class Employee(object):
  name = "Sam"
  company = "ILoveCode Inc."
  age = 30
  is_on_vacation = True

  def working(self, employee_name):
    self.name = employee_name
    print(f"{employee_name} is working")
```

Afterward, the `Employee` class can be imported into other files where new instances and methods can be created. This makes the code efficient, reusable, and maintainable:

```py
# other_file.py
from employee import Employee

def create_employee():
  print("Employee is starting their job...")
  employee1 = Employee()
  employee1.name = "Blake"
  employee1.working(employee1.name)

create_employee()
```

Running the code in `other_file.py` will output the following:

```
Employee is starting their job...
Blake is working
```