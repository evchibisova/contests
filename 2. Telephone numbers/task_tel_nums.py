def numbers_parser(numbers):
    """input: list of numbers
    output: refined list of numbers"""
    for i in range(len(numbers)):
        for sym in ["-", " ", "+", "(", ")"]:
            numbers[i] = numbers[i].replace(sym, "")
    return numbers


def patterns_parser(patterns):
    """input: list of patterns
    output: dict {refined number: - country operator"""
    patterns_dict = dict()
    for pattern in patterns:
        country, oper, num = pattern.split()[:3]
        key = country + oper + num
        for sym in ["-", " ", "+", "(", ")", "X"]:
            key = key.replace(sym, "")
        # {key: ["+COUNTRY_CODE OPERATOR_CODE ", "PERSONAL_NUMBER", " - COUNTRY OPER", pattern length, number length]}
        patterns_dict[key] = ["{} {} ".format(country, oper),
                              num,
                              pattern[pattern.index("-")-1:],
                              len(key) + num.count("X"),
                              len(num)]
    return patterns_dict


def solution(s):
    s = s.split("\n")
    numbers = numbers_parser(s[1:int(s[0])+1])
    patterns = patterns_parser(s[int(s[0]) + 2:])
    result = ""
    for number in numbers:
        for pattern in patterns:
            if len(number) == patterns[pattern][3] and pattern == number[:len(pattern)]:
                result += patterns[pattern][0] + number[-patterns[pattern][4]:] + patterns[pattern][2] + "\n"
                break
    result = result[:-1]    # delete last \n
    return result

