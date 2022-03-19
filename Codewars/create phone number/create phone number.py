def create_phone_number(n):
    n = list(map(str, n))
    return f"({''.join(n[:3])}) {''.join(n[3:6])}-{''.join(n[6:])}"


# solution
def create_phone_number_solution(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


txt3 = "My name is {}, I'm {}".format(*"xy")
print(txt3)

print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))