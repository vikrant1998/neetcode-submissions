class MinStack:

    def __init__(self):
        from collections import deque
        self.minstack = deque()
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.minstack) == 0: 
            self.minstack.append(val)
        else:
            if self.minstack[-1] < val:
                self.minstack.append(self.minstack[-1])
            else:
                self.minstack.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.arr[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]
        
