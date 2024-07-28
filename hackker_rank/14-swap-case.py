def swap_case(s):
    result: str = ""
    for i in s:
        if i == i.upper():
            result += i.lower()
        elif i == i.lower():
            result += i.upper()
        else:
            result += i
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
