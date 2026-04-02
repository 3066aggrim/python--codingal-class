def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("list of words with first and last character same ", lst)
    return ctr


count = match_words(['abc', 'sas', 'cdc', 'nep', 'hih'])
print("number of words having first  and last leters same:", count)
