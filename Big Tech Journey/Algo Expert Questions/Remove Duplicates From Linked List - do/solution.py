# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    curr = linkedList

    while curr is not None:
        runner = curr.next
        if curr.value == runner.value:
            curr.next = runner.next
        else:
            curr = runner
            runner = curr.next
    return linkedList
