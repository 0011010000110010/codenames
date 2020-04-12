
#? This code checks whether "harder_words file" has duplicate words. And counts how many words you have added until now.
# ! you are free to change "customized_harder_words.txt" for creating your own game words.

import random

with open("customized_harder_words.txt", "r", encoding="utf-8") as file:
    words = random.choice(file.readlines()).split(",")
    wordcount = {}
    for word in words:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    print(f"\nYou've added *{len(wordcount)}* until now.\nHere is your duplicated words;")
    for key in wordcount.keys():
        # print(f"{key}: {wordcount[key]}") # ? This code will show all words one by one, and it'll count them at the same time.
        if wordcount[key] > 1:
            print(key)

# ! if you see duplicated words, you can open "customized_harder_words.txt" file or "your_file". Then, press "ctrl+f" to type those words one by one. When you found them, change them or delete them. Do whatever you want.