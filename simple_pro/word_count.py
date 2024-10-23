from collections import Counter

text = input("Enter a any words: ")
words_count = Counter(text.split())

print(words_count)