def func_executor(*args):
    result = []
    for func_command, elements in args:
        function_process = func_command(*elements)
        result.append(f"{func_command.__name__} - {function_process}")
    return "\n".join(result)

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
