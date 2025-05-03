# collections.Counter

A **Counter** is a data type in the `collections` module. It is a [`dict`](./dict.md) subclass that stores counts for hashable objects. For each key-value pair, the key is the item being counted, and the value is the count of that object. A `Counter`‘s items are accessed just as in a dictionary, except accessing a missing key will return a `0` value rather than an error.

**Note:** A Counter will allow negative counts.

## Syntax
```py
myCollection = collections.Counter()
```

A `Counter` can also be initialized from an iterable or initialized from another mapping.

### Additional Methods
A `Counter` supplies the following additional methods beyond those for a standard dictionary:

- `.elements()`: Returns an iterator for the keys of the Counter repeating each element as many times as its count. It will ignore items with a count of less than one.
- `.most_common(n)`: Returns the n most common key-count pairs, in descending order of their counts. If n is omitted or None, the entire contents of the Collection are returned.
- `.subtract(values)`: Where values is an iterable or mapping. Matching keys have their values subtracted from the elements in the Counter. Inputs and outputs can be negative or zero.
- `.total()`: Returns the sum of all the counts.

Other differences from a standard dictionary:

- A `Counter` does not implement the [`.fromkeys()`](./dictionaries/from_keys.md) method.
- The [`.update()`](./dictionaries/update.md) method adds counter values rather than replacing them, making it the opposite of .subtract() above.

## Example
The following example creates a `Counter` from an iterable (a string) and outputs various characteristics of the `Counter`:
```py
import collections
c = collections.Counter("supercalifragilisticexpialidocious")
print(f"Counter Collection: {c}\n")
print(f"Sorted: {sorted(c.elements())}\n")
print(f"5 Most Common Items: {c.most_common(5)}")
```

Output
```text
Counter Collection: Counter({'i': 7, 's': 3, 'c': 3, 'a': 3, 'l': 3, 'u': 2, 'p': 2, 'e': 2, 'r': 2, 'o': 2, 'f': 1, 'g': 1, 't': 1, 'x': 1, 'd': 1})

Sorted: ['a', 'a', 'a', 'c', 'c', 'c', 'd', 'e', 'e', 'f', 'g', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'l', 'l', 'l', 'o', 'o', 'p', 'p', 'r', 'r', 's', 's', 's', 't', 'u', 'u', 'x']

5 Most Common Items: [('i', 7), ('s', 3), ('c', 3), ('a', 3), ('l', 3)]
```