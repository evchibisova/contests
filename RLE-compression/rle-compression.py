def solution(s):
    """main function, input: string from problem description, output: string with lengths"""
    s = s.split("\n")
    string = s[0]
    queries = s[2:]
    lens = ""
    for query in queries:
        start, end = query.split()
        lens += "{}\n".format(find_len(string, int(start), int(end)))
    lens = lens[:-1]
    return lens


def find_len(string, start, end):
    """find length of substring, input: base rle-string, int start and int end of range,
    output: length of rle-string"""
    end = end - start + 1
    range_list = make_range_list(string)
    # cut all before start
    while range_list:
        if start <= range_list[0]:
            range_list = [range_list[0] - start + 1] + range_list[1:]
            break
        start -= range_list[0]
        range_list = range_list[2:]

    # cut all after end
    pos = 0
    while pos < len(range_list):
        if end <= range_list[pos]:
            range_list = range_list[:pos+2]
            range_list[-2] = end
            break
        end -= range_list[pos]
        pos += 2

    range_list = [str(i) if i != 1 else "" for i in range_list]
    range_string = "".join(range_list)
    print(range_string)
    return len(range_string)


def make_range_list(string):
    """make a list from string, input: string, output: list,
    example: '2ab' transformed to [2, 'a', 1, 'b']"""
    range_list = []
    while string:
        pos = 0
        if not string[pos].isdigit():
            range_list.append(1)
        else:
            symbol_num = ""
            while string[pos].isdigit():
                symbol_num += string[pos]
                pos += 1
            range_list.append(int(symbol_num))
        range_list.append(string[pos])
        string = string[pos+1:]
    return range_list


inp = """a2bc3a
5
1 7
5 7
1 2
3 5
4 4"""

inp = """x1000000000yz
3
2 1000000001
2 1000000002
5938493 15938493"""

inp = """2c10b
1
1 12"""

print(solution(inp))

# with open("input.txt", "r") as inp:
# 	with open("output.txt", "w") as outp:
# 		outp.write(solution(inp.read()))