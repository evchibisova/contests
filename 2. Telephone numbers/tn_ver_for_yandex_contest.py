import sys

def solution(numbers, patterns):
    numbers = numbers_parser(numbers)
    patterns = patterns_parser(patterns)
    result = ""
    for number in numbers:
        for pattern in patterns:
            if len(number) == patterns[pattern][3] and pattern == number[:len(pattern)]:
                result += patterns[pattern][0] + number[-patterns[pattern][4]:] + patterns[pattern][2] + "\n"
                break
    result = result[:-1]
    return result


def numbers_parser(numbers):
    for i in range(len(numbers)):
        for sym in ["-", " ", "+", "(", ")"]:
            numbers[i] = numbers[i].replace(sym, "")
    return numbers


def patterns_parser(patterns):
    patterns_dict = dict()
    for pattern in patterns:
        country, oper, num = pattern.split()[:3]
        key = country + oper + num
        for sym in ["-", " ", "+", "(", ")", "X"]:
            key = key.replace(sym, "")
        patterns_dict[key] = ["{} {} ".format(country, oper),
                              num,
                              pattern[pattern.index("-")-1:],
                              len(key) + num.count("X"),
                              len(num)]
    return patterns_dict

num_count = int(sys.stdin.readline().strip())
numbers, patterns = [], []
for _ in range(num_count):
    numbers.append(sys.stdin.readline().strip())
pat_count = int(sys.stdin.readline().strip())
for _ in range(pat_count):
    patterns.append(sys.stdin.readline().strip())

print(solution(numbers, patterns))