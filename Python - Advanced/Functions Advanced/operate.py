def operate(operator, *args):
    def add(*args):
        return sum(args)
    def subtract(x, *args):
        return x + sum(-y for y in args)
    def divide(x, *args):
        result = x
        for z in args:
            result = result / z
        return result
    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result


    if operator == "+":
        return add(*args)
    if operator == "-":
        return subtract(*args)
    if operator == "/":
        return divide(*args)
    if operator == "*":
        return multiply(*args)
