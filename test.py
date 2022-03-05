def count(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return count(n - 1) + count(n - 2)


print(count(8))
