file = open('sampleText.txt', 'r')

content_words = (file.read()
                 .lower()
                 .replace(".", "")
                 .replace(",", "")
                 .replace(";", "")
                 .split())

words_map = {}

for word in content_words:
    if word in words_map:
        words_map.__setitem__(word, words_map[word] + 1)
        continue
    words_map.__setitem__(word, 1)

print(len([*content_words]))
print(sum(words_map.values()))

content_words_set = set(content_words)

print(len([*content_words_set]))
