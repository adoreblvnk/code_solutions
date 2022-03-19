def spin_words(sentence):
    sentence_list = sentence.split(" ")
    for i in range(len(sentence_list)):
        if len(sentence_list[i]) >= 5:
            sentence_list[i] = sentence_list[i][::-1]
    return " ".join(sentence_list)


# solution
def spin_words_solution(sentence):
    return " ".join([i[::-1] if len(i) >= 5 else i for i in sentence.split(" ")])

print(spin_words_solution("hey fellow kids"))