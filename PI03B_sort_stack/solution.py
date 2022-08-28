class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)


def sort_stack(stack: Stack) -> None:
    if not stack.is_empty():
        support_stack = Stack()
        support_stack.push(stack.pop())
        while not stack.is_empty():
            tmp = stack.pop()
            while support_stack.peek() > tmp:
                stack.push(support_stack.pop())
                if support_stack.is_empty():
                    break
            if support_stack.is_empty():
                support_stack.push(tmp)
            elif support_stack.peek() <= tmp:
                support_stack.push(tmp)
        while not support_stack.is_empty():
            stack.push(support_stack.pop())
    


if __name__ == "__main__":
    stack = Stack()
    stack.push(7)
    stack.push(10)
    stack.push(5)
    stack.push(3)
    stack.push(1)
    stack.push(8)
    stack.push(12)

    sort_stack(stack)

    while not stack.is_empty():
        print(stack.pop(), end=" -> ")

    stack2 = Stack()
    sort_stack(stack2)