def door_mat(n, m):
    for i in range(n // 2):
        j = int((2 * i) + 1)
        print(('.|.' * j).center(m, '-'))
    print('WELCOME'.center(m, '-'))
    for i in reversed(range(n // 2)):
        j = int((2 * i) + 1)
        print(('.|.' * j).center(m, '-'))


if __name__ == '__main__':
    n, m = map(int,input().split())
    door_mat(int(n), int(m))
