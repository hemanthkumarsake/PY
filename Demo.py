class Demo:
    def show(self,a=None,b=None,c=None):
        if a and b and c:
            print("3 arg")
        elif a and b:
            print("2 arg")
        elif a:
            print("1 arg")
        else:
            print("no arg")
a=Demo()
a.show()
a.show(2,3,4)
a.show(2,3)
a.show(2)