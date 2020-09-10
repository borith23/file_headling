#Use a for append to the end of the file
#Use .write for add new text to file .txt
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

#Use read() method for reading the content of the file
f = open("demofile.txt", "r")
print(f.read())


#Use w for overwrite
#Use w for create a new file if it does not exist:
x = open("demofile.txt", "w")
x.write("Hello new string")
x.close()

x = open("demofile.txt", "r")
print(x.read())