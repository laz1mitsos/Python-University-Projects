file = open("text.txt", 'r')
Vowels = ['a', 'i', 'u', 'e', 'o']

words = file.read().split()
words.sort(key = len)
words.reverse()

def vowelrem(string1):
    string1 = string1[::-1]
    for letter in string1:
        if letter in Vowels:
            string1 = string1.replace(letter, '')
    return string1

for i in range(5):
    print (vowelrem(words[i].strip()))
