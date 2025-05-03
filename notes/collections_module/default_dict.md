# defaultdict

In Python, **defaultdict** is a data type that belongs to the [`collections`](../collections_module.md) module. It is a [`dictionary`](../dictionaries.md) subclass that is used to return a dictionary-like object.

## Syntax
```py
collections.defaultdict(default_factory)
```
default_factory: It gives the default value for the dictionary object.

## Example
The following example demonstrates the `defaultdict` data type:

```py
from collections import defaultdict

def default_value():
  return "Not Declared"

myDefaultDict = defaultdict(default_value)

myDefaultDict["first"] = 100
myDefaultDict["second"] = 90

print(myDefaultDict["first"])
print(myDefaultDict["second"])
print(myDefaultDict["third"])
```

Here is the output for the above code:

```text
100
90
Not Declared
```