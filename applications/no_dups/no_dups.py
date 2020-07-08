def no_dups(s):
    word_count = {}
    # dict with number of words
    words = s.split()
    # list version of string
    results = ""
    # place to put "fixed" string
    for word in words:
        if word_count.__contains__(word) is False:
            # if the word does NOT exist in results, add it
             word_count[word] = 1
             results += f"{word} "
            #  else let it fly away into the infinite void. aka: "If it does exist in results, Fuck it"

    return results.rstrip()
    # return the fixed string
        




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))