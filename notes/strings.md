# Strings
A string is a sequence of characters contained within a pair of single quotes (') or double quotes("). Strings can store words, sentences, or whole paragraphs. They can be any length and can contain letters, numbers, symbols, and spaces.

```py
message1 = "I am a string"
message2 = 'I am also a string'
```

Other [data types](./data_types.md) such as integers, doubles, and booleans can also be strings if they are wrapped in quotes.

| Example | String? |
| ------- | ------- |
| "2" (with double-quotes) | Yes ✅ |
| '3.6' (with single-quotes) | Yes ✅ |
| "True" (also in quotes) | Yes ✅ |
| 7 (integer) | No ❌ |
| Hello (no quotes) | No ❌ |
| True (boolean) | No ❌ |

Strings are immutable; they cannot change. Every time an operation is performed on a string, a new string is created in memory.

## Accessing the Characters of a String
Strings in Python are technically a type of [list](./lists.md) — one in which each character is a separate element. This means each character in a string can be individually accessed by index, like with the elements in a list:
```py
myString = "Hello, World!"

var_1 = myString[0]
var_2 = myString[7:]
var_3 = myString[1:4]

print("var_1: " + var_1) # Output: var_1: H
print("var_2: " + var_2) # Output: var_2: World!
print("var_3: " + var_3) # Output: var_3: ell
```
If an attempt is made to access an index out of bounds, it will return an `IndexError`.
```py
name = "phillis"
name[8] # Throws an IndexError
```

## Multi-line Strings
Strings can be long or short. For longer text, a multi-line string can be used. Multi-line strings begin and end with three single or double quotes:

```py
my_string = """If it were done when 'tis done, then 'twere well
It were done quickly: if the assassination
Could trammel up the consequence, and catch
With his surcease success; that but this blow
Might be the be-all and the end-all here,
But here, upon this bank and shoal of time,
We'ld jump the life to come."""
```

## Escape Characters
Sometimes a string may have a character that Python tries to interpret, such as `'`.

```py
my_string = 'It's a lovely day!'

print(my_string)
```

This will raise an error, because the interpreter thinks the second `'` marks the end of the string.

```bash
  File "main.py", line 1
    my_string = 'It's a lovely day!'
                    ^
SyntaxError: invalid syntax
```

These characters can be “escaped” by adding a backslash beforehand. The `\` is called an escape character.

The backslash will not be visible if the string is printed:

```py
my_string = 'It\'s a lovely day!'

print(my_string)
# Output: It's a lovely day!
```

This problem can be avoided by wrapping strings containing `'` characters in double quotes:

```py
my_string = "It's a lovely day!"

print(my_string)
# Output: It's a lovely day!
```

Python also has a series of non-printing characters that can modify strings. For example, `\n` adds a new line and `\t` adds a tab:

```py
note = "I am on top!\nI am on bottom. \n\tI am indented!"

print(note)
```

This will output:

```bash
I am on top!
I am on bottom.
        I am indented!
```

## Modifying Strings

Python has special [operators](./operators.md) to modify strings. For example, `+` can be used to concatenate strings, and `*` can be used to multiply a string. The keyword in can be used to see if a given character or substring exists in a `string`.

```py
string_one = "Hello, "
string_two = "World! "
combo = string_one + string_two

print(combo)
# Output: Hello, World!

new_combo = combo * 2

print(new_combo)
# Output: Hello, World! Hello, World!

if "World" in new_combo:
  print("It's here!")
  # Output: It's here!
```

Strings can also be formatted with either of the following:

- The `f/F` flag (placed before the opening quotation mark).
- The [`.format()`](https://www.codecademy.com/resources/docs/python/strings/format) method (requires manually adding placeholders).

## Comparing Strings
Python can use comparison [operators](./operators.md) to compare the contents of two strings. The operators behave as they do with numeric arguments:

| Operator | Term | Description|
| -------- | ----- | ----------- |
| == |  Equal | Returns True if two strings are equal. |
| != |	Not equal |	Returns True if two strings are not equal. |
| <	 | Less than | Returns True if the left string is lexically prior the right string. |
| >	| Greater than |	Returns True is the left string comes lexically after the right string. |
| <= |	Less than or equal to |	Returns True if the left string is equal to or lexically prior to the right string. |
| >= |	Greater than or equal to |	Returns True if the left string is equal to or comes lexically after the right string. |

## Built-in String Methods
Python has a number of built-in string methods that manipulate strings. However, when these methods are called, the original string will not be changed, so any modifications will need to be saved to a new variable. A few useful built-in string methods are listed below.

### Strings
`.capitalize()`
Takes in a string, and returns a copy of the string in capital case.
`.casefold()`
Returns a copy of the string with all characters in lowercase.
`.center()`
Returns a new string with the specified padding.
`.count()`
Finds the number of times the specified substring occurs within a given string.
`.encode()`
Encodes a given string.
`.endswith()`
Checks whether or not a string ends with a given value.
`.find()`
Takes in a substring (and optionally start/end index), return the index number of the first occurrence of the substring inside a string.
`.format()`
Returns a string with values inserted via placeholders.
`.format_map()`
Returns the values from a given dictionary.
`.index()`
Searches through a string variable for the occurrence of a pattern or a substring.
`.isalnum()`
Returns True if all the characters in a given string are alphanumeric.
`.isalpha()`
Returns True if all characters in a string are letters of the alphabet, otherwise it returns False.
`.isascii()`
Returns True if all characters in a string are ASCII characters; otherwise, it returns False.
`.isdecimal()`
Checks whether a string consists of only decimal characters.
`.isdigit()`
Checks if all the elements in the string are digits and returns a boolean flag based on the result.
`.isidentifier()`
Takes in a string and returns True if the string is a valid Python identifier, else returns False.
`.islower()`
Takes in a string and returns True if all the letters in the string are in lowercase, else returns False. Ignores spaces, newlines, numeric and special characters in the string.
`.isnumeric()`
Verifies that all the characters within the string variable are numeric.
`.isprintable()`
Returns True if all characters in the string are printable or the string is empty, otherwise False if any character in the string is nonprintable.
`.isspace()`
Checks if all the characters in a string are whitespace characters.
`.istitle()`
Checks if a given string is in title case.
`.isupper()`
Takes in a string and returns True if all the letters in the string are in uppercase, else returns False. Ignores spaces, newlines, numeric and special characters in the string.
`.join()`
Concatenates all items from an iterable into a single string.
`.ljust()`
Left-aligns a string with a specified fill character
`.lower()`
Takes a string, and returns a copy of that string in which all letters are lowercase. Numbers and symbols are not changed.
`.lstrip()`
Removes leading characters from a string.
`.partition()`
Searches a string for a given keyword and splits that string into a three part tuple.
`.replace()`
Replace a specific substring with another substring.
`.rfind()`
Finds the last occurrence of a specified substring and returns the starting index.
`.rindex()`
Locates the highest index of the substring within a string variable.
`.rjust()`
Adds padding to the left of the given string.
`.rpartition()`
Used to split a string into three parts based on a specified separator.
`.rsplit()`
Splits a string into a list of substrings from the right end of the string based on a specified delimiter.
`.rstrip()`
Removes trailing characters from a string.
`.split()`
Breaks down a string into a list of substrings based on a specified separator.
`.splitlines()`
Used to split a multi-line string into a list of lines.
`.startswith()`
Checks whether a string starts with a specified value.
`.strip()`
Removes leading and trailing whitespace or specified characters from a string
`.swapcase()`
Takes a string and returns a copy of that string in which all lowercase letters are uppercase, and all uppercase letters are lowercase. Numbers and symbols are not changed.
`.title()`
Takes in a string and returns a copy of the string formatted in the title case: each word in the string is capitalized.
`.translate()`
Replaces characters in a string based on a mapping table.
`.upper()`
Takes a string, and returns a copy of that string in which all letters are uppercase. Numbers and symbols are not changed.
`.zfill()`
Returns a string with zeros padding the left side based on the integer given.
`maketrans()`
Returns a transition table based on the given strings.