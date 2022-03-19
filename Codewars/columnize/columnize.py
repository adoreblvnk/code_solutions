from itertools import zip_longest


def columnize(a, n):
    a = [a[i:i + n] for i in range(0, len(a), n)]
    b = [max(map(len, x)) for x in zip_longest(*a, fillvalue="")]
    return "\n".join(" | ".join(y.ljust(z) for y, z in zip(x, b)) for x in a)


print(columnize(["1", "12", "123", "1234", "12345", "123456"], 5))