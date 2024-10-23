from textblob import word

text = "Youur text with misspelled wrdds goes here."

corrected_text = " ".join(Word(word).correct() for word in text.split())

print(corrected_text)