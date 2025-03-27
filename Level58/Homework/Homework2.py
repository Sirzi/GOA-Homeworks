import math

def reduce_fraction(fraction):
    numerator, denominator = fraction
    gcd = math.gcd(numerator, denominator)
    return [numerator // gcd, denominator // gcd]


