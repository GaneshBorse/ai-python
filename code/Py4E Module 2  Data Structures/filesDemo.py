# print("helloo \nganesh")
# leng = "helloo\n ganesh"
# print(len(leng))

filehandler = open("filename.txt")
for line in filehandler:
    line = line.rstrip()
    if line.startswith("FROM:"):
        print(line)


filehandler = open("filename.txt")
for line in filehandler:
    line = line.rstrip()
    if not line.startswith("FROM:"):
        continue
    print(line)


fileName = input("Enter Name of file")
try:
    fhandler = open(fileName)
except:
    print("File name Incorrecxt")
    quit()  # imp
count = 0
for lines in fhandler:
    if lines.startswith("Starting of line"):
        count = count + 1
    print("there were", count, "lines")
