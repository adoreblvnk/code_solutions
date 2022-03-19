def high_and_low(numbers):
    string_numbers_in_list = numbers.split(" ")
    new_list = list()
    for i in string_numbers_in_list:
        new_list.append(int(i))
    max_number = max(new_list)
    min_number = min(new_list)
    return f"{max_number} {min_number}"
    # return f"{max(list(map(int, numbers.split(' '))))} {min(list(map(int, numbers.split(' '))))}"


# solution
def high_and_low_solution(numbers):
    return f"{max([int(s) for s in numbers.split(' ')])} {min([int(s) for s in numbers.split(' ')])}"


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
