class SinglylinklyQuene :
    class Node :
        def __init__(self,data,next = None):
            self.data = data
            self.next = next
    def __init__(self,__head = None,__tail = None,__length = 0):
        self.__head = __head
        self.__tail = __tail
        self.__length = __length
    def __is__empty(self,):
        return ((self.__head is None) and (self.__tail is None)) or (self.__length == 0)
    def __edit(self,data):
        node = self.Node(data)
        self.__head = node
        self.__tail = node
        self.__length += 1
    def enquene(self,data):
        if self.__is__empty() :
            return self.__edit(data)
        node = self.Node(data)
        self.__tail.next = node
        self.__tail = node
        self.__length += 1
    def dequene(self,):
        if not self.__is__empty() :
            values = self.__head.data
            self.__head = self.__head.next
            self.__length -= 1
            return values
    def top(self):
        return self.__head.data
    def length(self):
        return self.__length




