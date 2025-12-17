class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertionSortLinkedList(head):
    if not head or not head.next:
        return head

    sorted_list = None  
    current = head
    while current:
        next_node = current.next

        sorted_list = insertInSortedOrder(sorted_list, current)

        current = next_node 

    return sorted_list


def insertInSortedOrder(sorted_head, node):
    if not sorted_head or node.data < sorted_head.data:
        node.next = sorted_head
        return node

    current = sorted_head
    while current.next and current.next.data < node.data:
        current = current.next

    node.next = current.next
    current.next = node
    return sorted_head


def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()



head = Node(12)
head.next = Node(11)
head.next.next = Node(13)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)

sorted_head = insertionSortLinkedList(head)

printList(sorted_head)
