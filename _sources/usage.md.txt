# Usage and command line arguments

passwgen is a program with a command line interface. Let's look at the included help.

Assuming you are in the same directory as passwgen.py:

```text
python3 passwgen.py -h
---
usage: passwgen.py [-h] [-c] [-C] [-d] [-w] [-s] length

A program for generating random passwords.

positional arguments:
  length            length of the password to generate

optional arguments:
  -h, --help        show this help message and exit
  -c, --lowercase   include lowercase letters in the generated password
  -C, --uppercase   include uppercase letters in the generated password
  -d, --digits      include digits in the generated password
  -w, --whitespace  include whitespace characters in the generated password
  -s, --symbols     include symbols in the generated password
```

# Example

Let's say you want to create a password containing lowercase and uppercase letters and spaces with the length of 8.

Simply run:

```text
python3 passwgen.py 8 -cCw
---
ix ERiwA
```

Your generated password will be different due to the randomness, however, it will conform to given arguments.