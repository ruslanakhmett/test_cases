def number(value, operation=None):
    if operation is None:
        return value
    return operation(value)


def one(operation=None):
    return number(1, operation)


def two(operation=None):
    return number(2, operation)


def three(operation=None):
    return number(3, operation)


def four(operation=None):
    return number(4, operation)


def five(operation=None):
    return number(5, operation)


def plus(operand_second):
    return lambda operand_first: operand_first + operand_second


def minus(operand_second):
    return lambda operand_first: operand_first - operand_second


def umnojit(operand_second):
    return lambda operand_first: operand_first * operand_second


def delit(operand_second):
    return lambda operand_first: operand_first / operand_second


if __name__ == "__main__":
    print(two(plus(four())))  # 6
    print(one(delit(two())))  # 0,5
    print(two(plus(four(minus(three(umnojit(two())))))))  # 0
