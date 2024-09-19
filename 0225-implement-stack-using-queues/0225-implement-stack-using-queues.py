class MyStack:

    def __init__(self):
        self.q = collections.deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()        

    def top(self) -> int:
        right_val = self.q.pop()
        self.q.append(right_val)
        return right_val

    def empty(self) -> bool:
        return True if len(self.q) == 0 else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()