CounterDictRecord = {}

line = input("Enter a Line")

wordslist = line.split()

for word in wordslist:
    CounterDictRecord[word] = CounterDictRecord.get(word, 0) + 1

print(CounterDictRecord)
