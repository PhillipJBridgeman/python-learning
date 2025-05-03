# .update()

The `.update()` method returns new Python dictionary with entries from another dictionary, or some other iterable, added to it.

## Syntax

```py
dictionary.update(entries)
```

Where `entries` is another dictionary or an iterable of key-value pairs. Pairs in `dictionary` are replaced by any pair in `entries` with a duplicate key.

## Example
The following example creates two dictionaries, then adds the entries from one to the other.

```py
d1 = {1:'one',2:'two', 3:'three'}
d2 = {4:'four', 5:'five', 6:'six'}
d1.update(d2)
print(d1)
```

Output
```text
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
```