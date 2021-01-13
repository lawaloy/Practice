def partitionArr(strings):

    if not strings or len(strings) <=2:
        return strings

    result = []
    hashMap = {}
    for char in strings:
        hashMap[char] = hashMap.get(char, 0) +1

    for key,val in hashMap.items():
        result.append(key*val)

    return "".join(result)
print(partitionArr("bacbdabd"))
