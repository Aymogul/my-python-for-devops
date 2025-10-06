def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

maximum(12, 27, 36)

maximum(12.3, 45.6, 9.7)

maximum('yellow', 'red', 'orange')

maximum(13.5, -3, 7)

# Python’s Built-In max and min Functions
max('yellow', 'red', 'orange', 'blue', 'green')

min(15, 9, 27, 14)