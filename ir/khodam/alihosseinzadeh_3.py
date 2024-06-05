sentence = "Have a nice time in taking exam!"
word = "nice"

print(word + "  <-----existed?")
print(sentence.__contains__(word))

if(sentence.__contains__(word)):
    print("Its first index is:")
    print(sentence.index(word))