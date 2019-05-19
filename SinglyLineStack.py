class LinelyStack :
    def __init__(self,__size = 10,__count = 0):
        self.top = -1
        self.res = -1
        self.__size = __size
        self.__count = __count
        self.stack = [None] * self.__size
    def __is__empty(self,):
        return self.top == self.res
    def __is__fill(self,):
        return self.__count == self.__size
    def push(self,elem):
        if not self.__is__fill() :
            self.top += 1
            self.stack[self.top] = elem
            self.__count += 1
    def pop(self,):
        if not self.__is__empty() :
            self.res += 1
            __popNode = self.stack[self.top]
            self.__count -= 1
            return __popNode
    def top(self,):
        return self.stack[self.top]
