"""
You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default.
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.
Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
"""


myFile = open("myFile.txt","r")
name = myFile.readlines()
print(name)
print("共"+str(len(name))+"行")
myFile.close()

myFile = open("myFile.txt","w")
myFile.write("write new text")
myFile.close()