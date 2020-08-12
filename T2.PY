def main():
    print("Hellow")

if __name__=="__main__":
    main()

# Declare variables
f=0
# print(f)

# af="abc"
# print(af)

# print(str(f) + af)

def someFunction():
    global f
    f="def"
    print(f)

someFunction()
print(f)

# del f
# print(f)


def func1():
    print("hello navin")

func1()
print(func1())
print(func1)


#function take arguments
def func2(arg1,arg2):
    print(str(arg1) + "- " + str(arg2))
 
def cube(x):
    return x*x*x

func2(20,60)
print(func2(56,56))

print(cube(3))



def power(num, x=1):
    result=1
    for i in range(x):
        result=result * num
    return result

print(power(2))
print(power(5,2))


def conditional():
    x,y=100,1000
    if(x<y):
        st="x is less than y"
    elif(x==y):
        st="x is equal to y"
    else:
        st="x is greater than y"
    print(st)

conditional()


# Loops

def funcloop1():
    x=0
    while(x<5):
        print(x)
        x=x+1

funcloop1()

def forl():
    for x in range(5,10):
        print(x)
        
forl() 

days=["MON","TUE", "WED", "THUR","FIR", "SAT", "SUN"]
for d in days:
    print(d)

# enumerate index and value of collection
days=["MON","TUE", "WED", "THUR","FIR", "SAT", "SUN"]
for i,d in enumerate(days):
    print(i,d)

