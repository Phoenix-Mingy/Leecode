def isValid(s: str) -> bool:
    dictionary = {}
    for index, char in enumerate(s):
        dictionary[char] = index
    for num in dictionary.keys():
        if {"(", ")"}.issubset(dictionary.keys()):
            if (dictionary[")"] - dictionary["("]) % 2 == 0 and (dictionary[")"] - dictionary["("]) not in [1, -1]:
                return False
        elif {"[", "]"}.issubset(dictionary.keys()):
            if (dictionary["]"] - dictionary["["]) % 2 == 0 and (dictionary["]"] - dictionary["["]) not in [1, -1]:
                return False
        elif {"{", "}"}.issubset(dictionary.keys()):
            if (dictionary["}"] - dictionary["{"]) % 2 == 0 and (dictionary["}"] - dictionary["{"]) not in [1]:
                return False
        else:
            return False

    return True


print(isValid("(){}}{"))
