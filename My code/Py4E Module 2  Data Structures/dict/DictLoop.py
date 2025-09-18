dictname = {"key1": 123, "key2": 456, "chuck": 789, "freddyy": 000}
"""for key in dictname:
    print(key, dictname[key])
"""
for key, value in dictname.items():
    # dual iteration while using Items as it prints 2 values
    print(key, value)

print("converting to list then printing", list(dictname.keys()))
print("normal keys ", dictname.keys())
print("normal values", dictname.values())
print("normal items", dictname.items())
