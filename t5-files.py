def main():
    # create new file
    f = open("tdsf.txt","w+")
    
    for i in range(10):
        f.write("this is the " + str(i) + "\r\n")
    f.close() 

main()


def main2():
    # append existing file 
    f = open("tdsf.txt","a")
    
    for i in range(10):
        f.write("Appended data is the " + str(i) + "\r\n")
    f.close() 

main2()


def main3():
    # append existing file 
    f = open("tdsf.txt","r")
    if(f.mode=='r'):
        contents=f.read()
        print(contents)
    f.close() 

main3()