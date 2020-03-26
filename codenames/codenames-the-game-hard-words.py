import random

with open("hard_words_codenames.txt", "r", encoding="utf-8") as file:
    words = random.choice(file.readlines()).split(",")
    wordcount = {}
    for word in words:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    print(len(wordcount))
    for key in wordcount.keys():
        #print(f"{key}: {wordcount[key]}")
        if wordcount[key] > 1:
            print(key)
