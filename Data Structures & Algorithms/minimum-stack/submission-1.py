class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
            return
        cur_min = self.min_stack[-1]
        self.min_stack.append(val)
        if cur_min < val:
            self.min_stack[-1] = cur_min
            self.min_stack[-2] = val



    def pop(self) -> None:
        if not self.stack:
            return
        top = self.stack.pop()            
        if self.min_stack[-1] == top:
            self.min_stack.pop()
        else:
            temp = self.min_stack[-1]
            self.min_stack[-1] = self.min_stack[-2]
            self.min_stack[-2] = temp
            self.min_stack.pop()
            if len(self.min_stack) > 1:
                if self.min_stack[-1] > self.min_stack[-2]:
                    temp = self.min_stack[-1]
                    self.min_stack[-1] = self.min_stack[-2]
                    self.min_stack[-2] = temp


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
