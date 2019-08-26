# python3

import sys


class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, a):
        self.__stack.append(a)

    def pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

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

    def Max(self):
        assert(len(self.__stack))
        return self.max_stack.peek()


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
