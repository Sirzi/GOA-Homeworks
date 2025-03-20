def last_even_numbers(arr, number):
    even_numbers = [x for x in arr if x % 2 == 0]  # Filter even numbers
    return even_numbers[-number:]  # Return the last 'number' even numbers
