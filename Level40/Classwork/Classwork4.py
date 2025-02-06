def validate_pin(pin):
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)


print(validate_pin("1234"))