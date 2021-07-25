def func_print_decorator(function):
    def inner(a, b):
        print(f"I'm going to do '{function.__name__}' with '{a}' and '{b}'")
        return function(a, b)
    return inner


@func_print_decorator
def custom_sum(a: int, b: int) -> int:
    return a + b


@func_print_decorator
def multiply(a: int, b: int) -> int:
    return a * b


if __name__ == "__main__":
    print(custom_sum(2, 3) + 2)
    print(multiply(3, 5))
