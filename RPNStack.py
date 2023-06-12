class RPNStack():
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()
    
    def clear(self):
        self.stack = []

    def swap(self):
        if len(self.stack) > 1:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
    
    def dupLast(self):
        if len(self.stack):
            self.push(self.stack[-1])
        
    def print(self):
        for i in range(len(self.stack)):
            print(i + 1, " : ", self.stack[i])
    


    


