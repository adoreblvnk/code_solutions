def encrypt_this(text):  # failed
    words = text.split(" ")
    new_list = list()
    for i in words:
        if len(i) > 1:
            i = list(i)
            i[1], i[-1] = i[-1], i[1]
            i = "".join(i)
            new_list.append(f"{ord(i[0])}{i[1:]}")
        else:
            new_list.append(f"{ord(i[0])}")
    return new_list


# solution
def encrypt_this_solution(s):
    def swapper(w): return w if len(w) < 2 else w[-1] + w[1:-1] + w[0]
    return ' '.join(w if not w else str(ord(w[0])) + swapper(w[1:]) for w in s.split())


print(encrypt_this_solution("A wise old owl lived in an oak"))
