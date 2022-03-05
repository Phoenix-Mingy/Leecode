def romanToInt(s: str):
    dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for num, string in enumerate(s):
        if num > 0 and dictionary[string] > dictionary[s[num-1]]:
            result += dictionary[string] - 2*dictionary[s[num-1]]
        else:
            result += dictionary[string]
    return result


print(romanToInt("IV"))
