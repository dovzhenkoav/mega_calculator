from plus import plus
from minus import minus
from multiply import multiply
from division import division


def calculate(expression: str) -> int:
    existing_operations = '+-*/'
    for operation in existing_operations:
        if operation in expression:
            if expression.count(operation) == 1:
                match operation:
                    case '+':
                        return plus(expression)
                    case '-':
                        return minus(expression)
                    case '*':
                        return multiply(expression)
                    case '/':
                        return division(expression)
            else:
                raise ValueError('Должен быть только один знак!')
    raise ValueError(f'Операции в {expression} не знаем')

# if __name__ == '__main__':
#     print(calculate("1++1"))
#     # print('123431234'.count('+'))