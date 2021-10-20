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

            curNode = self.head
            for i in nodes:
                curNode.next = Node(i)
                curNode = curNode.next

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


ll = LinkedList(['a', 'b', 'c', 'd'])

for i in ll:
    print(i)

print(list(ll))
