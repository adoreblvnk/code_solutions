def duplicate_count(text):  # failed
    duplicate = 0
    for i in set(text):
        counting = text.lower().count(i)
        if counting > 1:
            duplicate += 1
    return duplicate


# solution
def duplicate_count_solution(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])


print(duplicate_count_solution("Indivisibilities"))