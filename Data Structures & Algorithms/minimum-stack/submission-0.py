class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if self.isempty():
            self.mins.append(val)
        else:
            if self.mins[len(self.mins)-1] > val:
                self.mins.append(val)
            else:
                self.mins.append(self.mins[len(self.mins)-1])
        self.stack.append(val)        
        
    def pop(self) -> None:
        self.mins.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def isempty(self):
        return len(self.stack) == 0

    def getMin(self) -> int:
        return self.mins[len(self.mins)-1]
        
