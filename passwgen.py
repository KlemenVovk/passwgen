from random import choices

class PasswordGenerator():
    # Lists of releveant indexes in the ASCII table.
    LOWERCASE_IXS = list(range(97,122 + 1)) 
    UPPERCASE_IXS = list(range(65,90 + 1))
    NUMBERS_IXS = list(range(48,57 + 1))
    SPACE_IX = [32]
    SYMBOLS_IXS = list(range(33,47 + 1)) + list(range(58,64 + 1)) + list(range(91,96 + 1)) + list(range(123, 126 + 1))

    # Depending on the given options, constructs a union of relevant indexes from above.
    def generate_relevant_ixs(self, options):
        population = []
        if options["hasLowercase"]: population += self.LOWERCASE_IXS
        if options["hasUppercase"]: population += self.UPPERCASE_IXS
        if options["hasNumbers"]: population += self.NUMBERS_IXS
        if options["hasSpaces"]: population += self.SPACE_IX
        if options["hasSymbols"]: population += self.SYMBOLS_IXS
        return population

    # FIXME Prevent spaces on the ends.
    # FIXME Make sure all chosen options are actually included if possible.
    def generate_password(self, length, options):
        population = self.generate_relevant_ixs(options)
        chosen_ixs = choices(population=population, k=length)
        return "".join([chr(ix) for ix in chosen_ixs])

options = {
    "hasLowercase": True,
    "hasUppercase": True,
    "hasNumbers": True,
    "hasSpaces": True,
    "hasSymbols": True
}
passgen = PasswordGenerator()
print(passgen.generate_password(10, options=options))