name = input("Enetr File name=")
fhandel = open(name)
lst = []

for line in fhandel:
    line = line.strip()
    words = line.split()
    for i in words:
        if i not in lst:
            lst.append(i)


lst.sort()
print(lst)

# Expected Output ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

""" input files conetent: 
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief"""
