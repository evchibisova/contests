def solution(input_data):
    result_dict, tops = make_pairs_list(input_data.split("\n")[1:])
    result = "{}\n{}".format(tops, len(result_dict))
    for i in result_dict:
        result += "\n{} {} {}".format(i[:3], i[3:], result_dict[i])
    return result


def make_pairs_list(string_list):
    """input: list of strings;
    output: dict of {word1word2: arc}, number of tops"""
    d = dict()
    tops_set = set()
    for s in string_list:
        for i in range(len(s) - 3):
            tops_set.update({s[i:i+3], s[i+1:i+4]})
            pair = s[i:i+3] + s[i+1:i+4]
            if pair not in d:
                d[pair] = 1
            else:
                d[pair] += 1
    return d, len(tops_set)
