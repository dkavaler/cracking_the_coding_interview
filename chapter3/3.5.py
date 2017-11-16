from mystack import MyStack

class SortedStack(MyStack):

    def __init__(self):
        MyStack.__init__(self)


    # Multiple ways to do this, you can cheese it 
    # by putting everything into an array, sorting the array,
    # then putting everything back into the stack (biggest first)
    def _sort_stack(self):
        elements = []
        while not super(SortedStack, self).is_empty():
            elements.append(super(SortedStack, self).pop())

        elements.sort(reverse=True)

        for el in elements:
            super(SortedStack, self).push(el)


    def push(self, d):
        super(SortedStack, self).push(d)
        self._sort_stack()


    # Using only stacks
    def push_2(self, d):
        temp_stack = MyStack()

        if super(SortedStack, self).is_empty():
            super(SortedStack, self).push(d)
            return

        while not super(SortedStack, self).is_empty() and super(SortedStack, self).peek() < d:
            temp_stack.push(super(SortedStack, self).pop())

        super(SortedStack, self).push(d)

        while not temp_stack.is_empty():
            super(SortedStack, self).push(temp_stack.pop())


    def pop(self):
        return super(SortedStack, self).pop()


    def peek(self):
        return super(SortedStack, self).peek()


    def is_empty(self):
        return super(SortedStack, self).is_empty()


if __name__ == '__main__':
    ss = SortedStack()
    ss.push(3)
    ss.push(4)
    ss.push(1)
    ss.push(10)
    ss.push(0)
    ss.push(5)

    assert not ss.is_empty()
    assert ss.peek() == 0
    assert ss.pop() == 0
    assert ss.pop() == 1
    assert ss.pop() == 3
    assert ss.pop() == 4
    assert ss.pop() == 5
    assert ss.pop() == 10


    ss = SortedStack()
    ss.push_2(3)
    ss.push_2(4)
    ss.push_2(1)
    ss.push_2(10)
    ss.push_2(0)
    ss.push_2(5)

    assert not ss.is_empty()
    assert ss.peek() == 0
    assert ss.pop() == 0
    assert ss.pop() == 1
    assert ss.pop() == 3
    assert ss.pop() == 4
    assert ss.pop() == 5
    assert ss.pop() == 10

