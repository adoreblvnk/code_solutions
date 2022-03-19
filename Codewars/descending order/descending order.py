def descending_order(num):
    num = list(map(int, str(num)))
    new_list = list()
    while num:
        new_list.append(max(num))
        num.remove(max(num))
    return int("".join(list(map(str, new_list))))


# solution
def descending_order_soln(num):
    return int("".join(sorted(str(num), reverse=True)))


print(descending_order(133))