def import_dict():
    with open('dict.txt', 'r') as file1:
        lines = [line.rstrip() for line in file1]
    return lines


def check():
    lines = import_dict()
    temp_list = lines
    for i in range(len(lines)-1):
        temp = list()
        len_lines = len(temp_list)
        #print(len_lines)
        while len_lines > 1:
            if (sorted(lines[i]) == sorted(temp_list[len_lines-1])):
                temp.append(temp_list[len_lines-1])
                temp_list.remove(temp_list[len_lines-1])
                len_lines = len_lines - 1
            len_lines = len_lines - 1
        if len(temp) > 1:
            print(' '.join(temp))


if __name__ == '__main__':
    check()