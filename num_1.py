# №1

# Первый вариант реализации функции с помощью линейного поиска
def zero_finder(arr: str) -> int:
    for i in range(len(arr)):
        print(f"Iteration #{i}\n")
        if arr[i] == '0':
            return i


# Второй вариант реализации функции с помощью бинарного поиска
def zero_finder_2(arr: str) -> int:
    n = len(arr) // 2
    cnt = 1
    while n < len(arr):
        if n == 2:
            n -= 1
        print(f"Iteration #{cnt}\n{n=}")
        if arr[n] == '1':
            if arr[n + 1] == '0':
                return n + 1
            else:
                n += n // (2 * cnt)
        else:
            if arr[n - 1] == '1':
                return n
            else:
                n -= n // (2 * cnt)
        cnt += 1
