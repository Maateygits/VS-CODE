while True:
    file = open("sinbo.txt" , "a")
    contents = file.write("More text!\n")
    print(contents)
file.close()