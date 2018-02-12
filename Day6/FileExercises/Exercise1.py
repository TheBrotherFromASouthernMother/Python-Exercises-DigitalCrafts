fileName = str(input("Please write the name of the file you would like to open: "))

file_handle = open(fileName, "r")
contents = file_handle.read()
file_handle.close()
print(contents)