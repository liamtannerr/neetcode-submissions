class OrderNode:

    def __init__(self, val=0, key=0, next: OrderNode=None, prev: OrderNode=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.left = OrderNode()
        self.right = OrderNode()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:

        if key not in self.cache:
            return - 1
        
        node = self.cache[key]
        self.moveToRight(node)

        return node.val

        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveToRight(node)
        else:
            node = OrderNode(value, key, self.right, self.right.prev)
            self.right.prev.next = node
            self.right.prev = node
            self.cache[key] = node
            if self.size == self.capacity:
                temp = self.left.next
                self.left.next = self.left.next.next
                temp.next.prev = self.left
                del self.cache[temp.key]
                del temp                
            else:
                self.size += 1


    def moveToRight(self, node:OrderNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.right.prev
        node.prev.next = node
        node.next = self.right
        self.right.prev = node

             
