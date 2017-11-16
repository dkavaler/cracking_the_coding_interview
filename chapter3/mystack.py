# Can use list as a stack, this is an exercise
class MyStack:

    class StackNode:

        def __init__(self, d):
            self.data = d
            self.next = None

    def __init__(self):
        self.top = None


    def pop(self):
        if self.top == None:
            return None

        d = self.top.data
        self.top = self.top.next

        return d

    def push(self, d):
        t = self.StackNode(d)
        t.next = self.top
        self.top = t

    def peek(self):
        if self.top == None:
            return None

        return self.top.data

    def is_empty(self):
        return self.top == None


    def as_list(self):
        sn = self.top
        ret_l = []
        while sn:
            ret_l.append(sn.data)
            sn = sn.next

        return ret_l


if __name__ == '__main__':
    s = MyStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    assert s.as_list() == [5, 4, 3, 2, 1]
    assert s.pop() == 5
    assert s.peek() == 4
    s.push(10)
    assert s.peek() == 10
    while not s.is_empty():
        s.pop()

    s.push(1)
    assert s.as_list() == [1]





