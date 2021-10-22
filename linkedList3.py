class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return self.data


class LinkedList:

    def __init__(self, nodes: list = None) -> None:
        """
        this function can take a list and convert it into linked list
        """

        self.head = None

        if nodes is not None:
            self.head = Node(nodes.pop(0))

            self.tail = self.head
            for i in nodes:
                self.tail.next = Node(i)
                self.tail = self.tail.next

    def __str__(self) -> str:
        node = self.head
        dataset = []
        while node is not None:
            dataset.append(node.data)
            node = node.next
        dataset.append("None")
        return " -> ".join(dataset)

    # traversing through linked list
    def __iter__(self):

        curNode = self.head
        while curNode is not None:
            yield curNode.data
            curNode = curNode.next

    # adding element to the beginning of the list
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    # adding element to the end of the list
    def append(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode


ll = LinkedList(['a', 'b', 'c', 'd', 'e'])

ll.push('e')
ll.push('f')
ll.push('g')

ll.append('k')
ll.append('p')
ll.append('z')

for index, data in enumerate(ll):
    print(index, data)

print(list(ll))

print(ll.tail.data)
