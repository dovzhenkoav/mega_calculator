from plus import plus
from minus import minus
from multiply import multiply
from division import division


def calculate(expression: str) -> int:
    existing_operations = '+-*/'
    for operation in existing_operations:
        if operation in expression:
            return {'+': plus(expression),
                    '-': minus(expression),
                    '*': multiply(expression),
                    '/': division(expression)}[operation]
    raise ValueError(f'Операции в {expression} не знаем')
