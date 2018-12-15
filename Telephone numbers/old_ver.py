with open("input.txt") as f:
    inp = f.read()


def solution(inp):
    s = inp.split('\n')
    nums = s[1:int(s[0])+1]
    patterns = s[int(s[0])+2:]
    pattern_list = []
    for p in patterns:
        pattern = []
        pattern.append(p[1:p.find(" ")])  #country code
        pattern.append(p[p.find("(")+1:p.find(")")])  #operator code
        pattern.append(p[p.find(") ") + 2: p.find("-") - 1])  #number digits
        pattern.append(p[p.find("-")+2:])  #country, operator
        pattern_list.append(pattern)

    answer = ""
    for i in range(len(nums)):
        symbols = "+- ()"
        for symbol in symbols:
            nums[i] = nums[i].replace(symbol, "")
        for pattern in pattern_list:
            if len(nums[i]) == len(pattern[0]+pattern[1]+pattern[2]):
                for j in range(3, 7):
                    if nums[i][:j] == pattern[0] + pattern[1]:
                        user_num = nums[i][j:]
                        for x in range(len(pattern[2])):
                            if pattern[2][x]!="X" and pattern[2][x] != user_num[x]:
                                break
                        else:
                            answer += "+{} ({}) {} - {}\n".format(pattern[0], pattern[1], user_num, pattern[3])

    answer = answer[:-1]
    return(answer)

with open("output.txt", "w") as out:
    out.write(solution(inp))