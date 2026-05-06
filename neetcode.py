from typing import List



def encode(strs: List[str]) -> str:
    res = ""
    for i in range(len(strs)):
        res += str((len(strs[i])))
        res +='%'
        res += (strs[i])
    return res

def decode(s: str) -> List[str]:
    res = []
    for i in range(len(s)):
        j = i
        while j != '%':
            continue
        length = int(s[i:j + 1])
        res.append(s[j : j + length])
        i = j + length
    return res


ls = ["Hello","World"]
encode(ls)
decode(ls)