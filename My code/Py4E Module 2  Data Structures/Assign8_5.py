fname = input("Enter file name: ")
fh = open(fname)
lst = []
count = 0
for line in fh:
    if line.startswith("From "):
        line.rstrip()
        x = line.split()
        print(x[1])
        count = count + 1

print("There were " + str(count) + " lines in the file with From as the first word")
