class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    # creates a new head and tail node
    def __init__(self):
        self.head = None
        self.tail = None
    # iteration

    def __iter__(self):
        node = self.head
        while node:
            yield node  # yield returns wihtout breaking the local variable
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode  # assigns newNode as tail node
            else:
                prevNode = self.head
                index = 0
                while index < location - 1:
                    prevNode = prevNode.next
                    index += 1
                nextNode = prevNode.next
                prevNode.next = newNode
                newNode.next = nextNode
                if prevNode == self.tail:
                    self.tail = newNode

    def traverseSLL(self):
        if self.head is None:
            print("The Single Linked List doesn't exist.")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def searchSLL(self, nodeValue):
        if self.head is None:
            return "The Single Linked List doesn't exist."
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "Value not found"


singleLinkedList = SLinkedList()
singleLinkedList.insertSLL(0, 0)
singleLinkedList.insertSLL(3, 1)
singleLinkedList.insertSLL(2, 2)

# print([node.value for node in singleLinkedList])

# singleLinkedList.traverseSLL()
print(singleLinkedList.searchSLL(3))
