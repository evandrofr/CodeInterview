class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

def find_intersection(head1: Node, head2: Node) -> Node:
    if not is_there_interseption:
        return None

    len1 = find_llist_length(head1)
    len2 = find_llist_length(head2)
    
    if len1 == len2:
        return find_intersection_same_len(head1, head2)
    else:
        if len1 > len2:
            bigger = head1
            smaller = head2
            jumps = len1 - len2
        else:
            bigger = head2
            smaller = head1
            jumps = len2 - len1
        
        while jumps > 0:
            bigger = bigger.next
            jumps -= 1
        
        return find_intersection_same_len(bigger, smaller)

def is_there_interseption(head1: Node, head2: Node) -> bool:
    c1 = head1
    while c1.next:
        c1 = c1.next
    c2 = head2
    while c2.next:
        c2 = c2.next
    return c1 == c2

def find_llist_length(head: Node) -> int:
    if head:
        current = head
        counter = 1
        while current.next:
            counter += 1
            current = current.next
        return counter
    return 0

def find_intersection_same_len(head1: Node, head2: Node) -> Node:
    if head1 and head2:
        c1 = head1
        c2 = head2

        while c1.next:
            if c1 == c2:
                return c1
            c1 = c1.next
            c2 = c2.next
    return None

if __name__ == "__main__":
    def pretty_print(head: Node) -> None:
        print(head.value, end=" -> ")
        current = head
        while current.next:
            current = current.next
            print(current.value, end=" -> ")
        print("\n")

    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)

    n0.next = n1
    n1.next = n2
    n2.next = n3

    n4.next = n5
    n5.next = n6

    n3.next = n7
    n6.next = n7

    n7.next = n8

    pretty_print(n0)
    pretty_print(n4)

    n = find_intersection(n0, n4)
    print(n.value)
    

    m = find_intersection(None, None)
    print(m)