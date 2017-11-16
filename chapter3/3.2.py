# Adapted from mystack.py to implement min in O(1) time.
# Assuming the stack only allows values that can be clearly compared
# with comparison operators (< == > etc)
class MyStack:

    class StackNode:

        def __init__(self, d):
            self.data = d
            self.next = None
            self.min_in_substack = None

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

        if not t.next or d < t.next.min_in_substack.data:
            t.min_in_substack = t
        else:
            t.min_in_substack = t.next.min_in_substack


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

    def min(self):
        if not self.top:
            return None
            
        return self.top.min_in_substack.data


if __name__ == '__main__':
    s = MyStack()
    s.push(5)
    assert s.min() == 5
    s.push(2)
    assert s.min() == 2
    s.push(1)
    assert s.min() == 1
    s.push(4)
    assert s.min() == 1
    s.push(3)
    assert s.min() == 1
    s.push(1)
    assert s.min() == 1
    s.pop()
    assert s.min() == 1
    s.pop()
    assert s.min() == 1
    s.pop()
    assert s.min() == 1
    s.pop()
    assert s.min() == 2
    s.pop()
    assert s.min() == 5


    





