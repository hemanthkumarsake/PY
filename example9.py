class Marks:
    def __init__(self,name,maths):
        self.__mathmarks=100
    def getMathmarks(self):
        return self.__mathmarks
    def setMathmarks(self, value):
        self.__mathmarks=value
s1=Marks("Hemanth", 100)
print(s1.getMathmarks())
s1.setMathmarks(99)
print(s1.getMathmarks())