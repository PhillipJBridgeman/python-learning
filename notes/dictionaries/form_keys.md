# .fromkeys()

The `.fromkeys()` method returns a dictionary with a specified set of keys. It can also initialize the entries with a specified value.

## Syntax

```py
dict.fromkeys(keys,value)
```

Where `keys` is an iterable containing the keys for the new dictionary and `value` is an optional initial value for the new entries in the dictionary. If `value` is not specified, the default initial value for each key will be `None`.

## Example
The following example creates a new dictionary with an initial value for each key.
```py
keylist = ('A', 'B', 'C', 'D')
value = 0
d = dict.fromkeys(keylist, value)
print(d)
```

Output
```text
{'A': 0, 'B': 0, 'C': 0, 'D': 0}
```