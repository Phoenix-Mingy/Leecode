def isPalindrome(x: int) -> bool:
    strings = str(x)
    for index, char in enumerate(strings):
        if char != strings[len(strings) - index - 1]:
            return False
    return True


print(isPalindrome(10))
