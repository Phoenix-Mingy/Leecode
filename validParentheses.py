def isValid(s: str) -> bool:
    lookup = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for parentheses in s:
        if parentheses in lookup:
            stack.append(parentheses)
        elif len(stack) == 0 or lookup[stack.pop()] != parentheses:
            return False
    return len(stack) == 0




