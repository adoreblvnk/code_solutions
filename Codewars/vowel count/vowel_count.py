def get_count(sentence):
    # write code here
    vowel_count = 0
    for vowel in "aeiouAEIOU":
        vowel_count += sentence.count(vowel)
    return vowel_count


# solution
get_count_solution = lambda sentence: sum(c in 'aeiouAEIOU' for c in sentence)

print(get_count("abcde"))