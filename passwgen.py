from random import choice, randint, shuffle
from itertools import groupby
import argparse


class PasswordGenerator():
    # Lists of releveant indexes in the ASCII table.
    LOWERCASE_IXS = list(range(97, 122 + 1))
    UPPERCASE_IXS = list(range(65, 90 + 1))
    DIGITS_IXS = list(range(48, 57 + 1))
    SPACE_IX = 32
    SYMBOLS_IXS = list(range(33, 47 + 1)) + list(range(58, 64 + 1)) + \
        list(range(91, 96 + 1)) + list(range(123, 126 + 1))

    # Deletes leading and trailing whitespace.
    def strip(self, passwd):
        while(passwd[0] == self.SPACE_IX or passwd[-1] == self.SPACE_IX):
            if(passwd[0] == self.SPACE_IX):
                del passwd[0]
            if(passwd[-1] == self.SPACE_IX):
                del passwd[-1]
        return passwd

    def generate_password(self, length, options):
        passwd = []
        # Generates random characters until given length is reached.
        while len(passwd) < length:
            # Uses round-robin for generating characters from specific chosen groups. This ensures that the result contains all selected groups if the length is sufficient.
            if options["hasLowercase"] and len(passwd) < length:
                passwd.append((choice(seq=self.LOWERCASE_IXS)))
            if options["hasUppercase"] and len(passwd) < length:
                passwd.append((choice(seq=self.UPPERCASE_IXS)))
            if options["hasDigits"] and len(passwd) < length:
                passwd.append((choice(seq=self.DIGITS_IXS)))
            if options["hasWhitespace"] and len(passwd) < length:
                passwd.append(self.SPACE_IX)
            if options["hasSymbols"] and len(passwd) < length:
                passwd.append((choice(seq=self.SYMBOLS_IXS)))

            # Shuffles the password, removes leading, trailing and consecutive whitespace.
            shuffle(passwd)
            passwd = self.strip(passwd)
            passwd = [x for x, y in groupby(passwd) if len(list(y)) < 2]

            # Ensures atleast 1 whitespace is in the password(stripping might have removed all whitespace).
            if(options["hasWhitespace"] and passwd.count(32) == 0):
                passwd.insert(randint(1, len(passwd) - 1), 32)

        return "".join([chr(ix) for ix in passwd])


def get_args():
    parser = argparse.ArgumentParser(description="A program for generating random passwords.")
    parser.add_argument(
        "length", help="length of the password to generate")
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


def parse_options():
    args = get_args()
    options = {
        "hasLowercase": args.lowercase,
        "hasUppercase": args.uppercase,
        "hasDigits": args.digits,
        "hasWhitespace": args.whitespace,
        "hasSymbols": args.symbols
    }

    # Should no options be selected, the generated password will contain lowercase and uppercase letters and digits.
    if(all(value == False for value in options.values())):
        options["hasLowercase"] = True
        options["hasUppercase"] = True
        options["hasDigits"] = True
    return options


passgen = PasswordGenerator()
print(passgen.generate_password(10, options=parse_options()))
