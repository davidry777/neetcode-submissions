class MinStack:

    def __init__(self):
        self.minStack_list = []

    def push(self, val: int) -> None:
        self.minStack_list.append(val)

    def pop(self) -> None:
        self.minStack_list.pop()

    def top(self) -> int:
        return self.minStack_list[-1]

    def getMin(self) -> int:
        return min(self.minStack_list)
