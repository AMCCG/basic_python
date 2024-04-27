if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = set(arr)
    print(arr1)
    arr2 = sorted(arr1)
    print(arr2)
    print(arr2[-2])
