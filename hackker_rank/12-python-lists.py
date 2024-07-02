if __name__ == '__main__':
    N = int(input())
    list_data = []
    for i in range(0, N):
        command = input()
        command_list = command.split(" ")
        if command_list[0] == "insert":
            list_data.insert(int(command_list[1]), int(command_list[2]))
        elif command_list[0] == "print":
            print(list_data, end="\n")
        elif command_list[0] == "remove":
            list_data.remove(int(command_list[1]))
        elif command_list[0] == "append":
            list_data.append(int(command_list[1]))
        elif command_list[0] == "sort":
            list_data.sort()
        elif command_list[0] == "pop":
            list_data.pop()
        elif command_list[0] == "reverse":
            list_data.reverse()
