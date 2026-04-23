from typing import List



def encode(strs: List[str]) -> str:
    res = ""
    for i in range(len(strs)):
        res += str((len(strs[i])))
        res +='%'
        res += (strs[i])
    return res

def decode(s: str) -> List[str]:
    return 0


ls = ["Hello","World"]
encode(ls)