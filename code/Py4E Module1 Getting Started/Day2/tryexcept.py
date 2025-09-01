astr = "Hello Bob"
try:
    iastr = int(astr)
    # here program blew up but due to except it proceeded forward. Inspite of challenges it faced. Truly a Champion
except:
    iastr = -1
print("first", iastr)  # here -1 is stored in iastr

bstr = "123"
try:
    ibstr = int(bstr)  # here 123 is stored in ibstr
except:
    ibstr = -1
print("second", ibstr)


############################################


# Below it will give Traceback error and stop at line2 so wont go forward

"""astr = "hello Bob"
istr = int(astr)  #ValueError: invalid literal for int() with base 10: 'hello Bob' ANd program wont procedd further , STOPS HERE!
print("first", istr)
astr = "123"
istr = int(astr)
print("second", istr)
"""
