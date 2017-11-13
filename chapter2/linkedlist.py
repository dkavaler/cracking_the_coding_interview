class ListNode:

    def __init__(self, d=None):
        self.next = None
        self.data = d


# Singly linked to make things harder
class LinkedList:

    def __init__(self, d=None):
        self.head = ListNode(d)

    def append(self, d):
        n = self.head
        while n.next:
            n = n.next

        n.next = ListNode(d)

    # 2.1 with buffer
    def remove_duplicates_wbuffer(self):
        buf = {}
        n = self.head
        prev = None

        while n:
            if n.data in buf:
                prev.next = n.next
            else:
                buf[n.data] = True
                prev = n
            n = n.next

    # 2.1 no buffer
    # Uses an extra pointer when compared to the book's solution,
    # but is similar to the wbuffer solution so easier to read in my opinion
    def remove_duplicates_nobuffer(self):
        n = self.head

        while n:
            ahead = n.next
            prev = n
            while ahead:
                if n.data == ahead.data:
                    prev.next = ahead.next
                else:
                    prev = ahead

                ahead = ahead.next

            n = n.next


def iterate_aggregate(ll):
    n = ll.head
    agg = []
    while n:
        agg.append(n.data)
        n = n.next

    return agg


def check_2_1_1(ll):
    ll.remove_duplicates_wbuffer()
    assert iterate_aggregate(ll) == [1, 2, 3, 4, 5]


def check_2_1_2(ll):
    ll.remove_duplicates_nobuffer()
    assert iterate_aggregate(ll) == [1, 2, 3, 4, 5]


def create_linkedlist():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(4)
    ll.append(5)
    ll.append(5)

    return ll

if __name__ == '__main__':
    ll = create_linkedlist()

    # 2.1 check
    check_2_1_1(ll)

    ll = create_linkedlist()
    check_2_1_2(ll)



