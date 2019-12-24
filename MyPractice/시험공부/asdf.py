def process(x):
    output = ''
    for ch in x :
        if (ch.isalpha()):
            output += ch
    return output.lower()
words = {}
filename = input('파일 명 : ')
file = open(filename,'r')
for line in file:
    linewords = line.split()
    for word in linewords:
        if process(word) in words.keys():
            words[process(word)] +=1
        else:
            words[process(word)] = 1
print(words)
