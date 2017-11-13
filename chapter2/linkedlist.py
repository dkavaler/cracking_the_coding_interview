class ListNode:

	def __init__(self, d=None):
		self.next = None
		self.data = d


class LinkedList:

	def __init__(self, d=None):
		self.head = ListNode(d)

	def append(self, d):
		n = self.head
		while n.next:
			n = n.next

		n.next = ListNode(d)
