def fake_bin(digits):
    return ''.join('1' if int(digit) >= 5 else '0' for digit in digits)


print(fake_bin("3456789"))
