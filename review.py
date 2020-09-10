#try block raises an error, the except block will be executed
try:
    #Use x for create new file
    #But it will error when it have file already
    x = open("myFile.txt", "x")
    x.write("Hello I'm created!!!") #Add text in file

    #Reading the content of the file
    x = open("myFile.txt", "r")
    print(x.read())
except:
    #Delete file
    import os
    if os.path.exists("myFile.txt"):
        os.remove("myFile.txt")
        print("Deleted !!!")
    else:
        print("The file does not exist")

