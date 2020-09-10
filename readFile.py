#Use open() function to return a file object
#Use r for read 
#Use read() method for reading the content of the file
f = open("demofile.txt", "r")
print(f.read())

#Use readline() method to return one line 
print(f.readline())

#Use loop to through the file line by line
for x in f:
    print(x)

#Use close() for close the file when you are finish
print(f.readline())
f.close()