def multiply(user_input):
    digits = []
    result = 0
    if "*" in user_input:
        for x in user_input:
            if x.isdigit():
                digits.append(x)
            else:
                continue
        for digit in digits:
            result *= int(digit)
        return result
