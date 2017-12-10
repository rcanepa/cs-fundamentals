class Fraction(object):
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __mul__(self, other):
        return Fraction(
            self.nominator * other.nominator,
            self.denominator * other.denominator
        )

    def __str__(self):
        return "{}/{}".format(self.nominator, self.denominator)


def __init__(self, nominator, denominator):
    self.nominator = nominator
    self.denominator = denominator


def __mul__(self, other):
    return Fraction(
        self.nominator * other.nominator,
        self.denominator * other.denominator
    )


def __str__(self):
    return "{}/{}".format(self.nominator, self.denominator)


attributes = {
    '__init__': __init__,
    '__mul__': __mul__,
    '__str__': __str__
}

FractionV2 = type("FractionV2", (object,), attributes)

if __name__ == "__main__":
    one_half = Fraction(1, 2)
    print(one_half)
    one_quarter = one_half * one_half
    print(one_quarter)
    print(type(Fraction))

    one_half = FractionV2(1, 2)
    print(one_half)
    one_quarter = one_half * one_half
    print(one_quarter)
    print(type(FractionV2))
