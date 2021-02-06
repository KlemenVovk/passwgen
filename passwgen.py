"""A small program for generating random passwords.

It supports choosing the included groups of characters(letters, numbers, symbols) and
the length of the generated password.
"""
__author__ = "Klemen Vovk"
__version__ = "1.0.0"
__license__ = "MIT"

from random import choice, randint, shuffle
from itertools import groupby
import argparse

# Lists of releveant indexes in the ASCII table.
LOWERCASE_IXS = list(range(97, 122 + 1))
UPPERCASE_IXS = list(range(65, 90 + 1))
DIGITS_IXS = list(range(48, 57 + 1))
SPACE_IX = 32
SYMBOLS_IXS = list(range(33, 47 + 1)) + list(range(58, 64 + 1)) + \
    list(range(91, 96 + 1)) + list(range(123, 126 + 1))


def _strip(passwd):
    # Deletes leading and trailing whitespace. Deletion is done based on the index of whitespace in the ASCII table 
    # as the password is still an array of ASCII table indexes at this point. This is used to prevent the password
    # from containg leading or trailing whitespace as that is hard to read and remember.

    while(passwd[0] == SPACE_IX or passwd[-1] == SPACE_IX):
        if(passwd[0] == SPACE_IX):
            del passwd[0]
        if(passwd[-1] == SPACE_IX):
            del passwd[-1]
    return passwd


def generate_password(options):
    """Genereates a password of given length containg groups of characters selected in given options.

    Generates a password of given length by using a round-robin approach to taking characters from selected
    groups in given options. This ensures that every selected group is included in the generated random password
    if the length of the password is more or equal to the number of selected groups.

    Args:
        options: 
            A dictionary holding the selected groups of characters to include in
            the generated password. The keys are "hasLowercase", "hasUppercase", "hasDigits", "hasWhitespace" and "hasSymbols".

    Returns:
        A string reperesenting the generated password.
    """
    passwd = []
    # Keeps generating random characters until the given length is reached.
    while len(passwd) < options["length"]:
        # Uses round-robin for generating characters from specific chosen groups. This ensures that the result contains all selected groups if the length is sufficient.
        if options["hasLowercase"] and len(passwd) < options["length"]:
            passwd.append((choice(seq=LOWERCASE_IXS)))
        if options["hasUppercase"] and len(passwd) < options["length"]:
            passwd.append((choice(seq=UPPERCASE_IXS)))
        if options["hasDigits"] and len(passwd) < options["length"]:
            passwd.append((choice(seq=DIGITS_IXS)))
        if options["hasWhitespace"] and len(passwd) < options["length"]:
            passwd.append(SPACE_IX)
        if options["hasSymbols"] and len(passwd) < options["length"]:
            passwd.append((choice(seq=SYMBOLS_IXS)))

        # Shuffles the password, removes leading, trailing and consecutive whitespace.
        shuffle(passwd)
        passwd = _strip(passwd)
        passwd = [x for x, y in groupby(passwd) if len(list(y)) < 2]

        # Ensures atleast 1 whitespace is in the password(stripping might have removed all whitespace).
        if(options["hasWhitespace"] and passwd.count(32) == 0):
            passwd.insert(randint(1, len(passwd) - 1), 32)

    return "".join([chr(ix) for ix in passwd])


def _get_args():
    # Uses to define and get given CLI arguments. Returns a namespace populated with arguments from the CLI.
    parser = argparse.ArgumentParser(
        description="A program for generating random passwords.")
    parser.add_argument(
        "length", help="length of the password to generate", type=int)
    parser.add_argument(
        "-c", "--lowercase", help="include lowercase letters in the generated password", action="store_true")
    parser.add_argument(
        "-C", "--uppercase", help="include uppercase letters in the generated password", action="store_true")
    parser.add_argument(
        "-d", "--digits", help="include digits in the generated password", action="store_true")
    parser.add_argument(
        "-w", "--whitespace", help="include whitespace characters in the generated password", action="store_true")
    parser.add_argument(
        "-s", "--symbols", help="include symbols in the generated password", action="store_true")
    return parser.parse_args()


def _parse_options():
    # Parses options to use in generation of the password from CLI arguments. If no options are given through the CLI arguments, the defaults are selected. 
    # By default "hasLowerCase", "hasUppercase" and "hasDigits" are True, all other are False.
    # Returns a dictionary holding selected options for password generation.
    # Raises ValueError: If the given length value is not positive.

    args = _get_args()
    options = {
        "length": args.length,
        "hasLowercase": args.lowercase,
        "hasUppercase": args.uppercase,
        "hasDigits": args.digits,
        "hasWhitespace": args.whitespace,
        "hasSymbols": args.symbols
    }

    if options["length"] <= 0:
        raise ValueError("Length must be a positive integer.")

    # Should no options be selected, the generated password will contain lowercase and uppercase letters and digits.
    if(all(value == False for value in filter(lambda x: isinstance(x, bool), options.values()))):
        options["hasLowercase"] = True
        options["hasUppercase"] = True
        options["hasDigits"] = True
    return options


def main():
    """Entry point for the program. Reads the arguments off of CLI.

    Returns:
        A generated random password.
    """
    passwd = generate_password(options=_parse_options())
    print(passwd)
    return passwd


if __name__ == "__main__":
    main()
