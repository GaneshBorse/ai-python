text = "X-DSPAM-Confidence:    0.8475"
col = text.find(":")
# print(col)
# print(len(text))

value = text[col + 1 : len(text)]
# print(value)

fvalue = value.strip()

num=float(fvalue)
print(fvalue)
""" 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
 Convert the extracted value to a floating point number and print it out."""
