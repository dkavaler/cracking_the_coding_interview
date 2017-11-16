from mystack import MyStack

class SetOfStacks:

	def __init__(self, capacity):
		self.stacks = [MyStack()]
		# Should have an error check here if capacity <= 0
		self.capacity = capacity
		self.stack_sizes = [0]


	def push(self, d):
		# Allocate a new stack if we need to
		if self.stack_sizes[-1] == self.capacity:
			self.stacks.append(MyStack())
			self.stack_sizes.append(0)

		self.stacks[-1].push(d)
		self.stack_sizes[-1] += 1


	def pop(self):
		if self.stacks[-1].is_empty():
			return None

		d = self.stacks[-1].pop()
		self.stack_sizes[-1] -= 1

		# Get rid of the stack to make things easier
		# O(1) in Python (a list can act as a stack)
		if self.stack_sizes[-1] == 0 and len(self.stacks) > 1:
			self.stacks.pop()
			self.stack_sizes.pop()

		return d


	def peek(self):
		if self.stack_sizes[-1] == 0:
			return None

		return self.stacks[-1].peek()


	def is_empty(self):
		return self.stack_sizes[0] == 0


	# This operates under the assumption that we don't need
	# all stacks at full capacity, which makes things much faster.
	def pop_at(self, index):
		if index >= len(self.stacks) or self.stack_sizes[index] == 0:
			return None

		self.stack_sizes[index] -= 1
		return self.stacks[index].pop()



if __name__ == '__main__':
	sos = SetOfStacks(3)
	sos.push(1)
	sos.push(2)
	sos.push(3)
	sos.push(4)
	sos.push(5)
	sos.push(6)

	assert sos.peek() == 6
	assert sos.pop() == 6
	assert sos.pop() == 5
	assert sos.peek() == 4
	assert sos.pop() == 4
	assert sos.peek() == 3
	assert sos.pop() == 3
	assert sos.pop() == 2
	assert sos.pop() == 1
	assert sos.pop() == None
	assert sos.pop() == None
	assert sos.peek() == None

	sos.push(1)
	sos.push(2)
	sos.push(3)
	sos.push(4)
	sos.push(5)
	sos.push(6)

	assert sos.peek() == 6
	assert sos.pop_at(0) == 3









