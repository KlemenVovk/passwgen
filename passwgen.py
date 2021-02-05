from random import choice, randint, shuffle
from itertools import groupby


class PasswordGenerator():
    # Lists of releveant indexes in the ASCII table.
    LOWERCASE_IXS = list(range(97, 122 + 1))
    UPPERCASE_IXS = list(range(65, 90 + 1))
    NUMBERS_IXS = list(range(48, 57 + 1))
    SPACE_IX = 32
    SYMBOLS_IXS = list(range(33, 47 + 1)) + list(range(58, 64 + 1)) + \
        list(range(91, 96 + 1)) + list(range(123, 126 + 1))

    def strip(self, passwd):
        while(passwd[0] == self.SPACE_IX or passwd[-1] == self.SPACE_IX):
            if(passwd[0] == self.SPACE_IX):
                del passwd[0]
            if(passwd[-1] == self.SPACE_IX):
                del passwd[-1]
        return passwd

    def generate_password(self, length, options):
        passwd = []
        # Generates random characters until given length is reached
        while len(passwd) < length:
            # Uses round-robin for generating characters from specific chosen groups. This ensures that the result contains all selected groups if the length is sufficient.
            if options["hasLowercase"] and len(passwd) < length:
                passwd.append((choice(seq=self.LOWERCASE_IXS)))
            if options["hasUppercase"] and len(passwd) < length:
                passwd.append((choice(seq=self.UPPERCASE_IXS)))
            if options["hasNumbers"] and len(passwd) < length:
                passwd.append((choice(seq=self.NUMBERS_IXS)))
            if options["hasSpaces"] and len(passwd) < length:
                passwd.append(self.SPACE_IX)
            if options["hasSymbols"] and len(passwd) < length:
                passwd.append((choice(seq=self.SYMBOLS_IXS)))

            # Shuffles the password, removes front and end spaces and removes consecutive spaces.
            shuffle(passwd)
            passwd = self.strip(passwd)
            passwd = [x for x, y in groupby(passwd) if len(list(y)) < 2]

            # Ensures atleast 1 space is in the password(removing adjacent spaces might have removed all spaces).
            if(options["hasSpaces"] and passwd.count(32) == 0):
                passwd.insert(randint(1, len(passwd) - 1), 32)

        return "".join([chr(ix) for ix in passwd])


options = {
    "hasLowercase": True,
    "hasUppercase": True,
    "hasNumbers": True,
    "hasSpaces": True,
    "hasSymbols": True
}
passgen = PasswordGenerator()
print(passgen.generate_password(10, options=options))
