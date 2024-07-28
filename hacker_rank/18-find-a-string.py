def count_substring(string, sub_string):
    total = 0
    length = len(string)
    for i in range(0, length):
        if string[i:length].startswith(sub_string):
            total += 1
    return total


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
