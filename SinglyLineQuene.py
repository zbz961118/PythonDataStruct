class LinelyQuene :

    def __init__(self,__length = 0,__size = 10):
        self.top = -1
        self.res = -1
        self.__size = __size
        self.__length = __length
        self.quene = [None] * self.__size
    def __is__empty(self,):
        return self.top == self.res
    def __is__fill(self,):
        return self.__length == self.__size
    def enquene(self,elem):
        if not self.__is__fill() :
            self.top += 1
            self.quene[self.top] = elem
            self.__length += 1
    def dequene(self,):
        if not self.__is__empty() :
            self.res += 1
            __popNode = self.quene[self.res]
            self.__length -= 1
            return __popNode
    def top(self,):
        return self.quene[self.top]



