count = {}
# print(type(ddd))

names = [
    "ganex",
    "hello",
    "hi",
    "hola",
    "bonjour",
    "ganex",
    "hello",
    "ganex",
    "hello",
    "hello",
    "hi",
    "hola",
    "bonjour",
    "ganex",
    "hello",
    "hello",
    "hi",
    "hello",
]
count["Greetings"] = " asjhg"
"""x = input("key name = ")
print(count.get(x, 0))"""

for name in names:
    count[name] = count.get(name, 0) + 1  # using .get()
print(count)

"""for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1"""
