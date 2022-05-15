# Definition for singly-linked list.
# import self as self


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = ListNode(val=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = ListNode(val=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.val)
            node = node.next
        return "".join(str(nodes))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        node = self
        nodes = []
        while node:
            nodes.append(node.val)
            node = node.next
        return "".join(str(nodes))
        # return str(self.val)


def reverseList(head: ListNode) -> ListNode:
    current,  prev = head, None
    while current:
        _next = current.next
        current.next = prev
        prev = current
        current = _next
    return prev


class Solution:
    def __init__(self):
        print("in init")


if __name__ == "__main__":
    testList = [1, 2, 3, 4, 5]
    llist = LinkedList(testList)

    # print(reverseList(llist.head))
    print(reverseList(llist.head))


