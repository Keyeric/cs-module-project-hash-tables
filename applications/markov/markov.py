import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
starting_chars = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
# A sentence can only start with a capital letter
ending_chars = {'.', '?', '!'}
# A sentence can only end with punctuation
word_dict = {}
# dictionary for words
index = -1
words_array = words.split()
# The almighty split to do the word busting for me
start = "starting_words"
previous_word = words_array[0]
# The previous word is the one first word 
word_dict[start] = []
remove_end = {'"', ':', ')'}
# punctuation at the end of words, eliminate
remove_front = {'('}
# punctuation at the front of words, eliminate
for word in words_array:
    # for every word in the split up string input
    if word[-1] in remove_end:
        # if the end of the word contains any eliminate targets
        word = word.replace(word[-1], "")
        # eliminate it
    if word[0] in remove_front:
        # if the front of the word contains any eliminate targets
        word = word.replace(word[0], "")
        # eliminate it

    if word[0] is '"' and word[1] in starting_chars:
        # if the first character in the word is a double quote (its speech) and the second character is a capital letter
        word_dict[start].append(word)
        # add the whole word to our word dict
    elif word[0] in starting_chars:
        # Else if the first character is a capital letter
        word_dict[start].append(word)
        # add it ti the word dict

    if word_dict.__contains__(word) is False:
        word_dict.setdefault(word, [])

    if index >= 0:
        word_dict[previous_word].append(word)
        previous_word = word
    index += 1


# TODO: construct 5 random sentences
sentences = []
while len(sentences) is not 5:
    starting_word = random.choice(word_dict[start])
    word = starting_word
    sentence = f"{starting_word} "
    while word[-1] not in ending_chars:
        word = random.choice(word_dict[word])
        if word in word_dict[start]:
            while word in word_dict[start]:
                word = random.choice(word_dict[word])
        sentence += f"{word} "
    sentences.append(sentence.rstrip())

for sentence in sentences:
    if sentence[0] is '"' and sentence[-1] is not '"':
        sentence += '"'
    print(sentence, end= "\n\n")