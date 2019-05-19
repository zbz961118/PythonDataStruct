class Dequene ():
    class Node :
        def __init__(self,elem,next = None,prev = None):
            self.elem = elem
            self.next = next
            self.prev = prev
    def __init__(self,__head = None,__tail = None,__length = 0):
        self.__head = __head
        self.__tail = __tail
        self.__length = __length
    def __is__empty(self,):
        return self.__head is None
    def __edit(self,elem):
        node = self.Node(elem)
        self.__head = node
        self.__tail = node
        self.__length += 1
    def lenquene(self,elem):
        if self.__is__empty() :
            return self.__edit(elem)
        node = self.Node(elem)
        node.next = self.__head
        self.__head.prev = node
        self.__head = node
    def ldequene(self,):
        if not self.__is__empty() :
            self.__head = self.__head.next
            self.__length -= 1
    def renquene(self,elem):
        if self.__is__empty() :
            return self.__edit(elem)
        node = self.Node(elem)
        self.__tail.next = node
        node.prev = self.__tail
        self.__tail = node
        self.__length += 1
    def ltop(self,):
        return self.__head.elem
    def rtop(self,):
        return self.__tail.elem
    def length(self, ):
        return self.__length


