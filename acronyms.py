acronyms = ["LOL", "IDK", "SMH", "OMG"]

acronyms.append("IMHO")

print(acronyms)

# acronyms.append("GTFO", "WTF") ---- won't work because list.append takes exactly 1 argument

acronyms.append("GTFO")

print(acronyms)

# methods (append) are called on objects (acronyms is our list object). the argument ("GTFO") is what we want to append to the list

acronyms.remove("LOL")
print(acronyms)

# OR to delete whatever item in a specific location...

del acronyms[3]

print(acronyms)


# check if exists in list
word = "BFF"

if word in acronyms:
    print(word + " is in the list")
else:
    print(word + " is NOT in the list!")


for acronym in acronyms:
    print(acronym)