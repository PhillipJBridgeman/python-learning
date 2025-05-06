# float()
The built-in `float()` function returns a float value based on a [string](../strings.md), numeric [data type](../data_types.md), or no value at all.

## Syntax
```py
float(num_string)
```
The `num_string` parameter is optional and should either be a string or numeric type.

## Example
In the example, the `float()` function is used to return float-type versions of an integer value `314` and a string `“314”`:

```py
print(float(314))
print(float("314"))
```

The following output will look like this:

```bash
314.0
314.0
```

## Codebyte Example
Use `float()` to create a new float value:
```py
f = float("1.23")
print(f)
```

## Output:
```bash
1.23
```