# .a2b_uu()
The `.a2b_uu()` [function](../functions.md) converts a single line of UUEncoded data back to binary and returns the binary data.

## Syntax

```py
binascii.a2b_uu(string)
```

- `string`: This parameter represents the UUEncoded data intended for decoding back into binary format. Specifically, it should be a Unicode string containing only ASCII characters and conforming to the UUEncode format.

## Example

```py
import binascii

# Inserting ASCII-encoded data in UUEncode format
encoded_data = '*0V]D96-A9&5M>0  \n'

# Decoding the ASCII-encoded data
decoded_data = binascii.a2b_uu(encoded_data)

# Printing the decoded message
print(decoded_data)
```

The above example produces the following output:

```text
b'Codecademy'
```