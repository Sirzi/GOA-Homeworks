def fake_bin(s):
    return ''.join('0' if int(digit) < 5 else '1' for digit in s)
