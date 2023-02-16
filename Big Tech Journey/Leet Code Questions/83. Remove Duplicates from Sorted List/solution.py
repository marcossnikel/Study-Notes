class Solution(object):
    def deleteDuplicates(self, head):
        currentNode = head

        while currentNode.next is not None:
            runner = currentNode.next
            if currentNode.val == runner.val:
                currentNode.next = runner.next
            else:
                currentNode = runner
                runner = currentNode.next
        return head