with open("myFile.txt","r+") as f:
    content = f.read()
    f.seek(0,0)
    f.write("q1use \"with\" open file\n" + content)