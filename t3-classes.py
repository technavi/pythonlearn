class myclass:
    def method1(self):
        print("myclass mehtod1")
    
    def method2(self,somestring):
        print("my class method2 " + somestring)

class anotherclass(myclass):
    def method1(self):
        print("another class method 1")
    def method2(self,somestring):
        print("method 2 " + somestring)


def main():
    c=myclass()
    c.method1()
    c.method2("sdf")
    ac=anotherclass()
    ac.method1()
    ac.method2("hello navin")


main() 