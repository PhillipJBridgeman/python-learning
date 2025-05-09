# namedtuple
A **namedtuple** is a data type in the `collections` module. It is a [`tuple`](../tuples.md) subclass that allows you to create immutable objects with named fields. This improves code readability by providing meaningful names for each element and making the code more explicit.

## Syntax
```py
namedtuple(typename, field_names)
```
- `typename`: The name of the new tuple subclass.
- `field_names`: It represents the names of the fields in the named tuple.

### Additional Methods
There are 3 specific namedtuple methods in addition to the standard methods inherited from tuples. All methods begin with an underscore to avoid conflicts with field names.

- `._make(iterable)`: (Class method) Creates a new instance based on an existing sequence or iterable.

- `._asdict()`: Returns a [`dict`](../dictionaries.md) with matching field names and values.

- `._replace(kwarg)`: Returns a new instance with fields replaced by the value provided as a keyword argument.

There are 2 specific attributes `._fields` and `_field_defaults` that will allow you respectively to list field names and to return a [`dict`](../dictionaries.md) with field names related to their default values.

## Example
In the following example, a namedtuple codecademyStudent with two fields (username and courses) to create two student instances is created. Two sentences will then be displayed about each student and their attributes.

```py
from collections import namedtuple

codecademyStudent = namedtuple('codecademyStudent', ['username', 'courses'])

student1 = codecademyStudent(username='Foo', courses=['Python', 'Computer Science'])
student2 = codecademyStudent(username='Bar', courses=['Javascript', 'Web Development'])

print("Student 1:", "Username:", student1.username, "| Courses involvement:", student1.courses)
print("Student 2:", "Username:", student2.username, "| Courses involvement:", student2.courses)
```

The above example results in the following output:

```text
Student 1: Username: Foo | Courses involvement: ['Python', 'Computer Science']
Student 2: Username: Bar | Courses involvement: ['Javascript', 'Web Development']
```