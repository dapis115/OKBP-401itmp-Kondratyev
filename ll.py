##Решение задач 1-30.


# Задача 1
def convert_types(data):
    result = []
    for item in data:
        if isinstance(item, str):
            try:
                result.append(int(item))
            except ValueError:
                try:
                    result.append(float(item))
                except ValueError:
                    result.append(item)
        elif isinstance(item, bool):
            result.append(str(item))
        elif isinstance(item, (int, float)):
            result.append(str(item))
        else:
            result.append(str(item))
    return result


# Задача 2
def swap_values(a, b):
    a, b = b, a
    return a, b


# Задача 3
def bool_transform(value):
    if value:
        return True
    else:
        return False


# Задача 4
def compound_operations(a, b):
    x = a
    x += b
    res_add = x
    x = a
    x -= b
    res_sub = x
    x = a
    x *= b
    res_mul = x
    x = a
    x /= b
    res_div = x
    x = a
    x //= b
    res_fdiv = x
    x = a
    x %= b
    res_mod = x
    x = a
    x **= b
    res_pow = x
    return [res_add, res_sub, res_mul, res_div, res_fdiv, res_mod, res_pow]


# Задача 5
def check_type(value, expected_type):
    mapping = {
        "int": int,
        "float": float,
        "str": str,
        "list": list,
        "bool": bool,
    }
    if expected_type not in mapping:
        return False
    return type(value) is mapping[expected_type]


# Задача 6
def logical_and(a, b, c):
    if a:
        if b:
            if c:
                return True
            return False
        return False
    return False


# Задача 7
def logical_or(a, b, c):
    if a:
        return True
    if b:
        return True
    if c:
        return True
    return False


# Задача 8
def is_between(value, low, high):
    if low <= value <= high:
        return True
    else:
        return False


# Задача 9
def print_even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)


# Задача 10
def countdown_while(n):
    i = n
    while i >= 1:
        print(i)
        i -= 1


# Задача 11
def skip_multiples(n, multiple):
    for i in range(1, n + 1):
        if i % multiple == 0:
            continue
        print(i)


# Задача 12
def if_elif_else_chain(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"


# Задача 13
def abs_value(x):
    if x < 0:
        return -x
    else:
        return x


# Задача 14
def binary_representation(n):
    if n == 0:
        return "0"
    sign = ""
    if n < 0:
        sign = "-"
        n = -n
    digits = ""
    while n > 0:
        digits = str(n % 2) + digits
        n //= 2
    return sign + digits


# Задача 15
def custom_round(number, ndigits):
    factor = 10 ** ndigits
    scaled = number * factor
    if scaled >= 0:
        rounded = int(scaled + 0.5)
    else:
        rounded = -int(-scaled + 0.5)
    return rounded / factor


# Задача 16
def find_max_min(numbers):
    max_value = numbers[0]
    min_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
        if n < min_value:
            min_value = n
    return max_value, min_value


# Задача 17
def all_true(iterable):
    for item in iterable:
        if not item:
            return False
    return True


# Задача 18
def any_true(iterable):
    for item in iterable:
        if item:
            return True
    return False


# Задача 19
def custom_enumerate(sequence, start=0):
    result = []
    index = start
    for element in sequence:
        result.append((index, element))
        index += 1
    return result


# Задача 20
def custom_filter(func, iterable):
    result = []
    for element in iterable:
        if func(element):
            result.append(element)
    return result


# Задача 21
def custom_map(func, iterable):
    result = []
    for element in iterable:
        result.append(func(element))
    return result


# Задача 22
def custom_zip(list1, list2):
    result = []
    for i in range(min(len(list1), len(list2))):
        result.append((list1[i], list2[i]))
    return result


# Задача 23
def custom_reversed(sequence):
    result = []
    for i in range(len(sequence) - 1, -1, -1):
        result.append(sequence[i])
    return result


# Задача 24
def custom_sorted(iterable, reverse=False):
    items = []
    for element in iterable:
        items.append(element)
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if reverse:
                swap_needed = items[j] < items[j + 1]
            else:
                swap_needed = items[j] > items[j + 1]
            if swap_needed:
                tmp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = tmp
    return items


# Задача 25
def sum_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


# Задача 26
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


# Задача 27
def power(base, exp):
    negative = exp < 0
    steps = -exp if negative else exp
    result = 1
    for _ in range(steps):
        result *= base
    if negative:
        return 1 / result
    return result


# Задача 28
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


# Задача 29
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Задача 30
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def show(number, title, call):
    print(f"--- Задача {number}: {title} ---")
    call()
    print()


def main():
    print("=" * 45)
    print("     РЕШЕНИЕ ЗАДАЧ 1-30")
    print("=" * 45)
    print()

    show(1, "convert_types", lambda: print(
        convert_types([1, "2", "hello", 3.5])))
    show(2, "swap_values", lambda: print(
        swap_values(5, 10)))
    show(3, "bool_transform", lambda: print(
        bool_transform(5), bool_transform(0)))
    show(4, "compound_operations", lambda: print(
        compound_operations(10, 3)))
    show(5, "check_type", lambda: print(
        check_type(5, 'int'), check_type("5", 'int')))
    show(6, "logical_and", lambda: print(
        logical_and(True, 5, "x"), logical_and(True, 0, "x")))
    show(7, "logical_or", lambda: print(
        logical_or(0, "", False), logical_or(0, 5, False)))
    show(8, "is_between", lambda: print(
        is_between(5, 1, 10), is_between(15, 1, 10)))
    show(9, "print_even_numbers", lambda: print_even_numbers(10))
    show(10, "countdown_while", lambda: countdown_while(5))
    show(11, "skip_multiples", lambda: skip_multiples(10, 3))
    show(12, "if_elif_else_chain", lambda: print(
        if_elif_else_chain(5), if_elif_else_chain(-3), if_elif_else_chain(0)))
    show(13, "abs_value", lambda: print(
        abs_value(-5), abs_value(3)))
    show(14, "binary_representation", lambda: print(
        binary_representation(10), binary_representation(0)))
    show(15, "custom_round", lambda: print(
        custom_round(3.14159, 2), custom_round(2.5, 0)))
    show(16, "find_max_min", lambda: print(
        find_max_min([3, 7, 1, 9, 2])))
    show(17, "all_true", lambda: print(
        all_true([1, 2, 3]), all_true([1, 0, 3])))
    show(18, "any_true", lambda: print(
        any_true([0, "", False]), any_true([0, 5, False])))
    show(19, "custom_enumerate", lambda: print(
        custom_enumerate(['a', 'b', 'c'], start=1)))
    show(20, "custom_filter", lambda: print(
        custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))
    show(21, "custom_map", lambda: print(
        custom_map(lambda x: x * 2, [1, 2, 3])))
    show(22, "custom_zip", lambda: print(
        custom_zip([1, 2, 3], ['a', 'b', 'c'])))
    show(23, "custom_reversed", lambda: print(
        custom_reversed([1, 2, 3, 4])))
    show(24, "custom_sorted", lambda: print(
        custom_sorted([3, 1, 4, 1, 5]), custom_sorted([3, 1, 4], reverse=True)))
    show(25, "sum_digits", lambda: print(
        sum_digits(1234), sum_digits(99)))
    show(26, "count_vowels", lambda: print(
        count_vowels("Hello World"), count_vowels("Python")))
    show(27, "power", lambda: print(
        power(2, 5), power(3, 3)))
    show(28, "is_prime", lambda: print(
        is_prime(17), is_prime(18)))
    show(29, "factorial", lambda: print(
        factorial(5), factorial(0)))
    show(30, "fibonacci", lambda: print(
        fibonacci(10), fibonacci(0), fibonacci(1)))


if __name__ == "__main__":
    main()
