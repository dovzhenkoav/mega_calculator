def plus(user_input):
    result = 0
    if "+" in user_input:
        digits = user_input.split("+")
        for f in digits:
            result += int(f)
        return result

