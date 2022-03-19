def get_middle(s):
    mid_i = int(len(s) // 2)
    if len(s) % 2 == 0:
        return s[mid_i - 1: mid_i + 1]
    return s[mid_i]


def get_middle_solution(s):
    return s[int((len(s) - 1) / 2):int(len(s) / 2 + 1)]


print(get_middle_solution("tes"))
