from mystack import MyStack

class MyQueue:

    def __init__(self):
        self.data_stack = MyStack()
        self.holder_stack = MyStack()


    def add(self, d):
        self.data_stack.push(d)


    def remove(self):
        self._transfer_data()
        d = self.holder_stack.pop()
        self._transfer_holder()

        return d

    def peek(self):
        self._transfer_data()
        d = self.holder_stack.peek()
        self._transfer_holder()


    def is_empty(self):
        return self.data_stack.is_empty()


    def _transfer_data(self):
        while not self.data_stack.is_empty():
            self.holder_stack.push(self.data_stack.pop())


    def _transfer_holder(self):
        while not self.holder_stack.is_empty():
            self.data_stack.push(self.holder_stack.pop())


if __name__ == '__main__':
    q = MyQueue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    q.add(5)

    assert q.remove() == 1
    assert q.remove() == 2
    assert q.remove() == 3
    assert q.remove() == 4
    assert q.remove() == 5

    