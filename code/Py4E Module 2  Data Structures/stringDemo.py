strdemo = "Helllo Wassup!"
# print(strdemo.find("H"))

# new = strdemo.replace("Wassup", "Ganex")
# print(new)

# lstrip() for LeftEnd whitespace remover and rshift() for RightEnd whitespaces.
# strip() removes from both end
# str1 = "    Hekjwh ad fdeswF      "
# print(str1.strip())

# str.startswith() returns true false
# print(strdemo.startswith("Helllo"))


# str.find("word/char", index to start from)
email = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = email.find("@")
print(atpos)

spacepos = email.find(" ", atpos)
print(spacepos)

host = email[atpos + 1 : spacepos]
print(host)
print(len(host) * 7)
