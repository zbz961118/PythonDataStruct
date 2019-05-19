class SinglylinkStack :
    class Node :
        def __init__(self,data,next =None):
            self.data = data
            self.next = next
    def __init__(self,__head = None,__size = 0):
        self.__head = __head
        self.__size = __size
    def __is__empty(self):
        return ((self.__head is None) and (self.__tail is None)) or (self.__size == 0)
    def __edit(self,data):
        node = self.Node(data)
        self.__head = node
        self.__size += 1
    def push(self,data):
        if self.__is__empty() :
            return self.__edit(data)
        node = self.Node(data)
        node.next = self.__head
        self.__head = node
        self.__size += 1
    def pop(self):
        if not self.__is__empty() :
            values = self.__head.data
            self.__head = self.__head.next
            self.__size -= 1
            return values
    def top(self):
        return self.__head.data
