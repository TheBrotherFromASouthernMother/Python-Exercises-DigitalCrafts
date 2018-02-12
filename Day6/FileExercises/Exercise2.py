fileName = str(input("Please write the name of the file you would like to open: "))

file_handle = open(fileName, "w")
contents = str(input("Please write the content you would like to save."))
file_handle.write(contents)
file_handle.close()
print(contents)