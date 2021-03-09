# put your code here.
f = open("test.txt")

words = f.read()

f.close()

counted_words = {}

for word in words.split():
    if word in counted_words:
        counted_words[word] += 1
    else:
        counted_words[word] = 1



for key, value in counted_words.items():
    print(key, value)