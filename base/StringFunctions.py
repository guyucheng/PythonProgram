#replace
string1 = "This is a new string"
string2 = string1.replace("new","old")
print(string2)


#join
print("join:")
print("|".join(["spam", "eggs", "ham"]))


#startswith
print("startswith:")
print("This is a sentence.".startswith("this"))

#endswith
print("sentence:")
print("This is a sentence.".endswith("sentence."))

#upper
print("This is a sentence.".upper())

#lower
print("AN ALL CAPS SENTENCE".lower())

#split
print("spam, eggs, ham".split(", "))
listA="spam, eggs, ham"
listB = listA.split(",")
print(listB)

