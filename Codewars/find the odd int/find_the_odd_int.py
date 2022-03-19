def find_it(seq):
    unique_seq = set(seq)
    for i in unique_seq:
        no_of_appearances = seq.count(i)
        if no_of_appearances % 2 == 1:
            return i


# solution
def find_it_solution(seq):
    return [x for x in set(seq) if seq.count(x) % 2][0]


print(find_it_solution([1, 1, 2, 3, 2]))

