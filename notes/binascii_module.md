# Binascii Module
The **`binascii`** module contains a number of methods to convert between binary and various ASCII-encoded binary representations. It is a valuable resource when dealing with binary data in various contexts, such as network protocols and file handling. Normally, a developer will not use these functions directly but use wrapper modules like uu or base64 instead. The binascii module contains low-level functions written in C for greater speed that are used by the higher-level modules. The Python binascii module is a valuable tool when working with binary data and encoding it into different text formats or decoding text representations back into binary data.

The following functions are provided by the `binascii` module:

## Binascii Module
[`.a2b_uu()`](./binascii_module/a2b_uu.md)
Returns a new object containing the decoded binary data from ASCII-encoded data in the UUEncode format.
[`.b2a_uu()`](./binascii_module/b2a_uu.md)
Converts binary data into a bytes object containing a string of ASCII characters in UUEncoded format.