def accum(s):
    return "-".join([(x * int(index + 1)).title() for (index, x) in enumerate(s)])


# solution
def accum_solution(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))

print(accum_solution("aBcd"))
