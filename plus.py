def plus(user_input):
    digits = []
    result = 0
    if "+" in user_input:
        for f in user_input:
            if f.isdigit():
                digits.append(f)
            else:
                continue
        for digit in digits:
            result += int(digit)
        return result


