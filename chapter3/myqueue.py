# Can implement this with Python list. This is an exercise

class MyQueue:

	class QueueNode:

		def __init__(self, d):
			self.data = d
			self.next = None



	def __init__(self):
		self.first = None
		self.last = None


	def add(self, d):
		qn = self.QueueNode(d)
		if self.last:
			self.last.next = qn
		
		self.last = qn

		if not self.first:
			self.first = self.last


	def remove(self):
		if not self.first:
			return None

		d = self.first.data
		self.first = self.first.next

		if not self.first:
			self.last = None

		return d


	def peek(self):
		if not self.first:
			return None

		return self.first.data


	def is_empty(self):
		return not self.first


	def as_list(self):
		ret_l = []
		qn = self.first
		while qn:
			ret_l.append(qn.data)
			qn = qn.next

		return ret_l


if __name__ == '__main__':
	q = MyQueue()
	q.add(1)
	q.add(2)
	q.add(3)
	q.add(4)
	q.add(5)

	assert q.as_list() == [1, 2, 3, 4, 5]

	assert q.remove() == 1
	assert q.as_list() == [2, 3, 4, 5]
	assert q.peek() == 2
	assert not q.is_empty()

	while not q.is_empty():
		q.remove()

	assert q.as_list() == []
