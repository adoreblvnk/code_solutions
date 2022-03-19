# positive_sum = lambda arr: sum(i for i in arr if i > 0)


def positive_sum(arr):
    # write code here
    total_sum = 0
    for x in arr:
        if x > 0:
            total_sum += x
    return total_sum

print(positive_sum([1, -4, 7, 12]))  # console: 20
print(positive_sum([1, 2, -4, -88]))  # console: 3