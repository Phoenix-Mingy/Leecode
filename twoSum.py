def two_sum(num, targets) -> list:
    for number1, i in enumerate(num):
        for number2, j in enumerate(num):
            if i + j == targets and number1 != number2:
                return [number1, number2]


nums = [3, 2, 4]
target = 6

a = two_sum(nums, target)
print(a)
