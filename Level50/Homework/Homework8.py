def printer_error(control_string):
    errors = sum(1 for char in control_string if char < 'a' or char > 'm')
    total_length = len(control_string)
    return f"{errors}/{total_length}"