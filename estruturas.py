class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len (self.items) -1]

class Node:
    def __init__(self, dado=0, p_node=None):
        self.dado = dado
        self.next = p_node

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.next)
        
class Lista_Encad:

    def __init__(self):
        self.head = None
        self._size = 0
    
    def __repr__(self):
        r = ''
        point = self.head
        while point:
            r = r + str(point.dado) + ', '
            point = point.next
        return r
    
    def __str__(self):
        return self.__repr__()

    def isEmpty(self):
        if self._size == 0:
            return True

    def add_final(self, elem):
        if self.head:
            point = self.head
            while point.next:
                point = point.next
            point.next = Node(elem) 
        else:
            self.head = Node(elem)
        self._size += 1

    def __len__(self):
        return self._size
    
    def _get_node(self,index):
        point = self.head
        for i in range(index):
            if point:
                point = point.next
            else:
                raise IndentationError('index fora de alcance')
        return point
        

    def __getitem__(self,index):
        point = self._get_node(index)
        if point:
            return point.dado
        raise IndentationError("index fora de alcance")
 
    def __setitem__(self,index,elem):
        point = self._get_node(index)
        if point:
            point.dado = elem
        else:
            raise IndexError("indext fora de alcance")

    def index(self,elem):
        point = self.head
        i = 0
        while point:
            if point.dado == elem:
                return i
            point = point.next
            i += 1
        raise ValueError (f'{elem}: nao esta na lista')
    
    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node = Node(elem)
            node.next = self.head
            self.head = node
        else:
            point = self._get_node(index-1)
            node.next = point.next
            point.next = node
        self._size += 1
    
    def remove(self,elem):
        if self.head == None:
            raise ValueError(f'{elem}: nao esta na lista')
        elif self.head.dado == elem:
            self.head == self.head.next
        else:
            anc = self.head
            point = self.head.next
            while point:
                if point.dado == elem:
                    anc.next = point.next
                    point.next = None
                anc = point
                point = point.next
            self._size -= 1
            return True
        raise ValueError(f'{elem}: nao esta na lista')

