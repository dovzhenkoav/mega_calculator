
def minus(user):
    """Вычетание"""
    digits = []
    result = 0
    if "-" in user:
        for i in user:
            if i.isdigit():
                digits.append(i)
            else:
                continue
        for digit in digits:
            result -= int(digit)
        return result


