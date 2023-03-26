def multiply(user_input):
    result = 1
    for digit in user_input.split("*"):
        result *= int(digit)
    return result
