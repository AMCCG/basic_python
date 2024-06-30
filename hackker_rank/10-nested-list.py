if __name__ == '__main__':
    list_student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_student.append([name, score])
    second_highest = sorted(set([score for name, score in list_student]))[1]
    print('\n'.join(sorted([name for name, score in list_student if score == second_highest])))
