# Take a sentence in English and turn it into the same sentence in Pig Latin!

sentence = input()
words = sentence.split()
transl = ""
for w in words:
    transl += w[1:] + w[0] + "ay "

print(transl[:-1])