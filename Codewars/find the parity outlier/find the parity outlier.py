def find_outlier(integers):
    evens_first = sorted(integers, key=lambda x: x % 2)
    if evens_first[1] % 2 == 1:
        return evens_first[0]
    return evens_first[-1]


def find_outlier_soln(integers):
    parity = [n % 2 for n in integers]
    print(parity)
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]


print(find_outlier_soln([160, 3, 1719, 19, 11, 13, -21]))
print(find_outlier_soln([2, 4, 6, 8, 10, 3]))