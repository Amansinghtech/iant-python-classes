class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return self.data


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        node = self.head
        dataset = []
        while node is not None:
            dataset.append(node.data)
            node = node.next
        dataset.append("None")
        return " -> ".join(dataset)


ll = LinkedList()

first = Node('a')
second = Node('b')
third = Node('c')

ll.head = first
first.next = second
second.next = third

print(ll)
