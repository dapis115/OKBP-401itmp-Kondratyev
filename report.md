# Лабораторная работа 2 — Решение задач 1–30

**Источник заданий:** `Dokument Microsoft Word.docx`
**Файл с решением:** `ll.py`
**Запуск:** `python ll.py`

---

## Задача 1

**Вопрос:** Напишите функцию `convert_types(data)`, которая принимает список и возвращает новый список, где каждый элемент преобразован: числа в строки, строки в числа (если возможно), остальные элементы — в строковое представление.

*Подсказка:* Используйте try-except для безопасного преобразования строк в числа.

**Решение:**

```python
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
```

**Ответ:** Функция возвращает преобразованный список.

```text
convert_types([1, "2", "hello", 3.5]) → ['1', 2, 'hello', '3.5']
```

---

## Задача 2

**Вопрос:** Напишите функцию `swap_values(a, b)`, которая меняет значения двух переменных местами без использования третьей переменной и возвращает кортеж `(a, b)`.

*Подсказка:* Используйте множественное присваивание Python.

**Решение:**

```python
def swap_values(a, b):
    a, b = b, a
    return a, b
```

**Ответ:** Функция возвращает кортеж с обменёнными значениями.

```text
swap_values(5, 10) → (10, 5)
```

---

## Задача 3

**Вопрос:** Напишите функцию `bool_transform(value)`, которая возвращает `True`, если значение «истинное» (не 0, не пустое), и `False` иначе, без использования `bool()`.

*Подсказка:* Используйте условный оператор.

**Решение:**

```python
def bool_transform(value):
    if value:
        return True
    else:
        return False
```

**Ответ:** Функция возвращает `True` или `False`.

```text
bool_transform(5) → True, bool_transform(0) → False
```

---

## Задача 4

**Вопрос:** Напишите функцию `compound_operations(a, b)`, которая выполняет все составные операции (`+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`) над `a` со значением `b` и возвращает список результатов.

*Подсказка:* Создайте копию `a` для каждой операции.

**Решение:**

```python
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
```

**Ответ:** Функция возвращает список из 7 результатов операций.

```text
compound_operations(10, 3) → [13, 7, 30, 3.3333333333333335, 3, 1, 1000]
```

---

## Задача 5

**Вопрос:** Напишите функцию `check_type(value, expected_type)`, которая проверяет, соответствует ли тип `value` ожидаемому типу (строка `'int'`, `'float'`, `'str'`, `'list'`, `'bool'`), и возвращает `True` или `False`.

*Подсказка:* Используйте `type()` и `type().__name__`.

**Решение:**

```python
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
```

**Ответ:** Функция возвращает `True` или `False`.

```text
check_type(5, 'int') → True, check_type("5", 'int') → False
```

---

## Задача 6

**Вопрос:** Напишите функцию `logical_and(a, b, c)`, которая возвращает `True`, только если все три аргумента «истинные», без использования оператора `and`.

*Подсказка:* Используйте вложенные `if`.

**Решение:**

```python
def logical_and(a, b, c):
    if a:
        if b:
            if c:
                return True
            return False
        return False
    return False
```

**Ответ:** Функция возвращает `True` или `False`.

```text
logical_and(True, 5, "x") → True, logical_and(True, 0, "x") → False
```

---

## Задача 7

**Вопрос:** Напишите функцию `logical_or(a, b, c)`, которая возвращает `True`, если хотя бы один аргумент «истинный», без использования оператора `or`.

*Подсказка:* Используйте несколько `if` с ранним возвратом.

**Решение:**

```python
def logical_or(a, b, c):
    if a:
        return True
    if b:
        return True
    if c:
        return True
    return False
```

**Ответ:** Функция возвращает `True` или `False`.

```text
logical_or(0, "", False) → False, logical_or(0, 5, False) → True
```

---

## Задача 8

**Вопрос:** Напишите функцию `is_between(value, low, high)`, которая проверяет, находится ли `value` между `low` и `high` (включительно), используя один составной условный оператор.

*Подсказка:* Используйте `and` в условии `if`.

**Решение:**

```python
def is_between(value, low, high):
    if low <= value <= high:
        return True
    else:
        return False
```

**Ответ:** Функция возвращает `True` или `False`.

```text
is_between(5, 1, 10) → True, is_between(15, 1, 10) → False
```

---

## Задача 9

**Вопрос:** Напишите функцию `print_even_numbers(n)`, которая выводит все чётные числа от 1 до `n` включительно, используя цикл `for`.

*Подсказка:* Используйте `range()` с шагом 2 или проверку `% 2`.

**Решение:**

```python
def print_even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)
```

**Ответ:** Функция выводит в консоль чётные числа.

```text
print_even_numbers(10) →
2
4
6
8
10
```

---

## Задача 10

**Вопрос:** Напишите функцию `countdown_while(n)`, которая выводит числа от `n` до 1 в обратном порядке, используя цикл `while`.

*Подсказка:* Уменьшайте счётчик внутри цикла.

**Решение:**

```python
def countdown_while(n):
    i = n
    while i >= 1:
        print(i)
        i -= 1
```

**Ответ:** Функция выводит в консоль числа в обратном порядке.

```text
countdown_while(5) →
5
4
3
2
1
```

---

## Задача 11

**Вопрос:** Напишите функцию `skip_multiples(n, multiple)`, которая выводит числа от 1 до `n`, но пропускает числа, делящиеся на `multiple`, используя `continue`.

*Подсказка:* Проверка `if i % multiple == 0: continue`.

**Решение:**

```python
def skip_multiples(n, multiple):
    for i in range(1, n + 1):
        if i % multiple == 0:
            continue
        print(i)
```

**Ответ:** Функция выводит в консоль числа, пропуская кратные.

```text
skip_multiples(10, 3) →
1
2
4
5
7
8
10
```

---

## Задача 12

**Вопрос:** Напишите функцию `if_elif_else_chain(x)`, которая возвращает `"positive"`, если `x > 0`, `"negative"`, если `x < 0`, `"zero"`, если `x == 0`. Используйте полную конструкцию `if-elif-else`.

*Подсказка:* Три ветви условия.

**Решение:**

```python
def if_elif_else_chain(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"
```

**Ответ:** Функция возвращает строку.

```text
if_elif_else_chain(5) → "positive"
if_elif_else_chain(-3) → "negative"
if_elif_else_chain(0) → "zero"
```

---

## Задача 13

**Вопрос:** Напишите функцию `abs_value(x)`, которая возвращает абсолютное значение числа без использования `abs()`.

*Подсказка:* Используйте условный оператор.

**Решение:**

```python
def abs_value(x):
    if x < 0:
        return -x
    else:
        return x
```

**Ответ:** Функция возвращает неотрицательное число.

```text
abs_value(-5) → 5, abs_value(3) → 3
```

---

## Задача 14

**Вопрос:** Напишите функцию `binary_representation(n)`, которая возвращает двоичное представление числа в виде строки без использования `bin()`.

*Подсказка:* Делите на 2 и собирайте остатки.

**Решение:**

```python
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
```

**Ответ:** Функция возвращает строку с двоичным представлением.

```text
binary_representation(10) → "1010", binary_representation(0) → "0"
```

---

## Задача 15

**Вопрос:** Напишите функцию `custom_round(number, ndigits)`, которая округляет число до `ndigits` знаков после запятой без использования `round()`.

*Подсказка:* Умножьте на `10**ndigits`, округлите через `int()`, разделите обратно.

**Решение:**

```python
def custom_round(number, ndigits):
    factor = 10 ** ndigits
    scaled = number * factor
    if scaled >= 0:
        rounded = int(scaled + 0.5)
    else:
        rounded = -int(-scaled + 0.5)
    return rounded / factor
```

**Ответ:** Функция возвращает округлённое число.

```text
custom_round(3.14159, 2) → 3.14, custom_round(2.5, 0) → 3.0
```

---

## Задача 16

**Вопрос:** Напишите функцию `find_max_min(numbers)`, которая возвращает кортеж `(max_value, min_value)` списка без использования `max()` и `min()`.

*Подсказка:* Пройдитесь по списку циклом.

**Решение:**

```python
def find_max_min(numbers):
    max_value = numbers[0]
    min_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
        if n < min_value:
            min_value = n
    return max_value, min_value
```

**Ответ:** Функция возвращает кортеж из двух чисел.

```text
find_max_min([3, 7, 1, 9, 2]) → (9, 1)
```

---

## Задача 17

**Вопрос:** Напишите функцию `all_true(iterable)`, которая возвращает `True`, если все элементы «истинные», без использования `all()`.

*Подсказка:* Верните `False` при первом «ложном» элементе.

**Решение:**

```python
def all_true(iterable):
    for item in iterable:
        if not item:
            return False
    return True
```

**Ответ:** Функция возвращает `True` или `False`.

```text
all_true([1, 2, 3]) → True, all_true([1, 0, 3]) → False
```

---

## Задача 18

**Вопрос:** Напишите функцию `any_true(iterable)`, которая возвращает `True`, если хотя бы один элемент «истинный», без использования `any()`.

*Подсказка:* Верните `True` при первом «истинном» элементе.

**Решение:**

```python
def any_true(iterable):
    for item in iterable:
        if item:
            return True
    return False
```

**Ответ:** Функция возвращает `True` или `False`.

```text
any_true([0, "", False]) → False, any_true([0, 5, False]) → True
```

---

## Задача 19

**Вопрос:** Напишите функцию `custom_enumerate(sequence, start=0)`, которая возвращает список кортежей `(index, element)`, без использования `enumerate()`.

*Подсказка:* Используйте счётчик в цикле.

**Решение:**

```python
def custom_enumerate(sequence, start=0):
    result = []
    index = start
    for element in sequence:
        result.append((index, element))
        index += 1
    return result
```

**Ответ:** Функция возвращает список кортежей.

```text
custom_enumerate(['a', 'b', 'c'], start=1) → [(1, 'a'), (2, 'b'), (3, 'c')]
```

---

## Задача 20

**Вопрос:** Напишите функцию `custom_filter(func, iterable)`, которая возвращает список элементов, для которых `func(element)` возвращает `True`, без использования `filter()`.

*Подсказка:* Проверяйте каждый элемент в цикле.

**Решение:**

```python
def custom_filter(func, iterable):
    result = []
    for element in iterable:
        if func(element):
            result.append(element)
    return result
```

**Ответ:** Функция возвращает список отфильтрованных элементов.

```text
custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) → [2, 4]
```

---

## Задача 21

**Вопрос:** Напишите функцию `custom_map(func, iterable)`, которая применяет `func` к каждому элементу и возвращает список результатов, без использования `map()`.

*Подсказка:* Вызывайте функцию для каждого элемента.

**Решение:**

```python
def custom_map(func, iterable):
    result = []
    for element in iterable:
        result.append(func(element))
    return result
```

**Ответ:** Функция возвращает список преобразованных элементов.

```text
custom_map(lambda x: x * 2, [1, 2, 3]) → [2, 4, 6]
```

---

## Задача 22

**Вопрос:** Напишите функцию `custom_zip(list1, list2)`, которая возвращает список кортежей из пар элементов, без использования `zip()`.

*Подсказка:* Используйте `min(len(list1), len(list2))` для ограничения.

**Решение:**

```python
def custom_zip(list1, list2):
    result = []
    for i in range(min(len(list1), len(list2))):
        result.append((list1[i], list2[i]))
    return result
```

**Ответ:** Функция возвращает список кортежей.

```text
custom_zip([1, 2, 3], ['a', 'b', 'c']) → [(1, 'a'), (2, 'b'), (3, 'c')]
```

---

## Задача 23

**Вопрос:** Напишите функцию `custom_reversed(sequence)`, которая возвращает развёрнутый список, без использования `reversed()` и срезов `[::-1]`.

*Подсказка:* Идите от конца к началу циклом.

**Решение:**

```python
def custom_reversed(sequence):
    result = []
    for i in range(len(sequence) - 1, -1, -1):
        result.append(sequence[i])
    return result
```

**Ответ:** Функция возвращает развёрнутый список.

```text
custom_reversed([1, 2, 3, 4]) → [4, 3, 2, 1]
```

---

## Задача 24

**Вопрос:** Напишите функцию `custom_sorted(iterable, reverse=False)`, которая возвращает отсортированный список, без использования `sorted()` и `.sort()`.

*Подсказка:* Реализуйте простую сортировку пузырьком.

**Решение:**

```python
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
```

**Ответ:** Функция возвращает отсортированный список.

```text
custom_sorted([3, 1, 4, 1, 5]) → [1, 1, 3, 4, 5]
custom_sorted([3, 1, 4], reverse=True) → [4, 3, 1]
```

---

## Задача 25

**Вопрос:** Напишите функцию `sum_digits(n)`, которая возвращает сумму цифр числа, используя цикл `while`.

*Подсказка:* Извлекайте цифры через `% 10` и `// 10`.

**Решение:**

```python
def sum_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
```

**Ответ:** Функция возвращает сумму цифр (целое число).

```text
sum_digits(1234) → 10, sum_digits(99) → 18
```

---

## Задача 26

**Вопрос:** Напишите функцию `count_vowels(text)`, которая подсчитывает количество гласных букв в строке (без учёта регистра).

*Подсказка:* Используйте строку `'aeiouAEIOU'` и цикл `for`.

**Решение:**

```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count
```

**Ответ:** Функция возвращает количество гласных (целое число).

```text
count_vowels("Hello World") → 3, count_vowels("Python") → 1
```

---

## Задача 27

**Вопрос:** Напишите функцию `power(base, exp)`, которая возводит `base` в степень `exp`, без использования `**` и `pow()`, используя цикл.

*Подсказка:* Умножайте `base` на себя `exp` раз.

**Решение:**

```python
def power(base, exp):
    negative = exp < 0
    steps = -exp if negative else exp
    result = 1
    for _ in range(steps):
        result *= base
    if negative:
        return 1 / result
    return result
```

**Ответ:** Функция возвращает результат возведения в степень (число).

```text
power(2, 5) → 32, power(3, 3) → 27
```

---

## Задача 28

**Вопрос:** Напишите функцию `is_prime(n)`, которая проверяет, является ли число простым, используя цикл `for`.

*Подсказка:* Проверяйте делители от 2 до `sqrt(n)`.

**Решение:**

```python
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
```

**Ответ:** Функция возвращает `True` или `False`.

```text
is_prime(17) → True, is_prime(18) → False
```

---

## Задача 29

**Вопрос:** Напишите функцию `factorial(n)`, которая вычисляет факториал числа, используя цикл `for` или `while`.

*Подсказка:* `n! = 1 * 2 * 3 * ... * n`.

**Решение:**

```python
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

**Ответ:** Функция возвращает факториал (целое число).

```text
factorial(5) → 120, factorial(0) → 1
```

---

## Задача 30

**Вопрос:** Напишите функцию `fibonacci(n)`, которая возвращает n-е число Фибоначчи, используя цикл `for`.

*Подсказка:* Храните два предыдущих числа и обновляйте их.

**Решение:**

```python
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

**Ответ:** Функция возвращает n-е число Фибоначчи (целое число).

```text
fibonacci(10) → 55, fibonacci(0) → 0, fibonacci(1) → 1
```

---

## Полный вывод программы `ll.py`

```text
=============================================
     РЕШЕНИЕ ЗАДАЧ 1-30
=============================================

--- Задача 1: convert_types ---
['1', 2, 'hello', '3.5']

--- Задача 2: swap_values ---
(10, 5)

--- Задача 3: bool_transform ---
True False

--- Задача 4: compound_operations ---
[13, 7, 30, 3.3333333333333335, 3, 1, 1000]

--- Задача 5: check_type ---
True False

--- Задача 6: logical_and ---
True False

--- Задача 7: logical_or ---
False True

--- Задача 8: is_between ---
True False

--- Задача 9: print_even_numbers ---
2
4
6
8
10

--- Задача 10: countdown_while ---
5
4
3
2
1

--- Задача 11: skip_multiples ---
1
2
4
5
7
8
10

--- Задача 12: if_elif_else_chain ---
positive negative zero

--- Задача 13: abs_value ---
5 3

--- Задача 14: binary_representation ---
1010 0

--- Задача 15: custom_round ---
3.14 3.0

--- Задача 16: find_max_min ---
(9, 1)

--- Задача 17: all_true ---
True False

--- Задача 18: any_true ---
False True

--- Задача 19: custom_enumerate ---
[(1, 'a'), (2, 'b'), (3, 'c')]

--- Задача 20: custom_filter ---
[2, 4]

--- Задача 21: custom_map ---
[2, 4, 6]

--- Задача 22: custom_zip ---
[(1, 'a'), (2, 'b'), (3, 'c')]

--- Задача 23: custom_reversed ---
[4, 3, 2, 1]

--- Задача 24: custom_sorted ---
[1, 1, 3, 4, 5] [4, 3, 1]

--- Задача 25: sum_digits ---
10 18

--- Задача 26: count_vowels ---
3 1

--- Задача 27: power ---
32 27

--- Задача 28: is_prime ---
True False

--- Задача 29: factorial ---
120 1

--- Задача 30: fibonacci ---
55 0 1
```
