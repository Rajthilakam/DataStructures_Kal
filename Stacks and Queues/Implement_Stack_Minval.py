

class MinStack:
    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, val: int) :
        self.stack.append(val)
        val = min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(val) 

    def pop(self) :
        pop = self.stack.pop()
        if self.minstack[-1] == pop:
            self.minstack.pop()

    def top(self) :
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.minstack[-1]