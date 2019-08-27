# python3

from collections import deque


class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, a):
        self.__stack.append(a)

    def pop(self):
        assert(len(self.__stack))
        return self.__stack.pop()

    def empty(self):
        return len(self.__stack) == 0

    def peek(self):
        assert(len(self.__stack))
        return self.__stack[-1]


class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.max_stack = Stack()

    def Push(self, a):
        self.__stack.append(a)
        if self.max_stack.empty():
            self.max_stack.push(a)
        else:
            cur_max = self.max_stack.peek()
            if cur_max is not None and cur_max <= a:
                self.max_stack.push(a)

    def Pop(self):
        assert(len(self.__stack))
        cur_top = self.__stack.pop()
        cur_max = self.max_stack.peek()
        if cur_max == cur_top:
            self.max_stack.pop()
        return cur_top

    def Max(self):
        assert(len(self.__stack))
        return self.max_stack.peek()

    def Empty(self):
        return len(self.__stack) == 0


def max_sliding_window_naive(sequence, m):
    res = []
    stack_1 = StackWithMax()
    stack_2 = StackWithMax()

    for idx, cur_item in enumerate(sequence):
        if idx < m:
            stack_1.Push(cur_item)
        else:
            while not stack_1.Empty():
                stack_2.Push(stack_1.Pop())
            res.append(stack_2.Max())

            stack_2.Pop()

            while not stack_2.Empty():
                stack_1.Push(stack_2.Pop())
            stack_1.Push(cur_item)

    while not stack_1.Empty():
        stack_2.Push(stack_1.Pop())
    res.append(stack_2.Max())

    return res


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))
