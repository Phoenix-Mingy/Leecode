def longestCommonPrefix(strs) -> str:
    if strs == "":
        return strs

    for i in range(len(strs[0])):
        for strings in strs[1:]:
            if i >= len(strings) or strings[i] != strs[0][i]:
                return strs[0][:i]


longestCommonPrefix()