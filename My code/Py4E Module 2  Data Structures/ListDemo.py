friends = ["ganesh", "abc", "xyz"]
print(friends)


# for friend in friends:
#    print("happy neew year:", friend)


"""print(list(range(len(friends))))
for i in range(len(friends)):
    print("happy new year:", i, friends[i])"""


friends.insert(1, "one")  # needs (pos, value)


n2 = ["hello", "hi"]
friends.extend(n2)

friends.append("vola")
# print(friends)
# friends.pop(0)
# print(friends)
# friends.remove("vola")
# print(friends)

# "abc" in friends


# print("abc" in friends)


friends.sort(reverse=True)
print(friends)

numlist = list()
while True:
    inp = input("Enter No.")
    if inp.lower() == "done":
        break
    value = float(inp)
    numlist.append(value)
avg = sum(numlist) / len(numlist)
print(avg)
