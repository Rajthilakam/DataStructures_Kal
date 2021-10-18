

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
        print(self.minstack[-1])
        return self.minstack[-1]

if __name__ == '__main__':
    m = MinStack()
    m.push(5)
    m.push(3)
    m.pop()
    m.push(4)
    m.getMin()
