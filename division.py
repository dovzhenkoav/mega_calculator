def division(expression: str) -> int:
    values: list = expression.split('/')
    values = [int(i) for i in values]

    if values[1] == 0:
        raise ZeroDivisionError('Нихуя! На ноль делить нельзя')

    return int(values[0] / values[1])


if __name__ == '__main__':
    print(division('-28/0'))
