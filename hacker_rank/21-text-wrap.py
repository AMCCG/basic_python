import textwrap


def wrap(string, max_width):
    word_wrap: string = ""
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(string)
    for element in word_list:
        word_wrap += element + "\n"
    return word_wrap


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
