class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.mini = val
        else:
            self.stack.append(val - self.mini)
            self.mini = min(self.mini, val)

    def pop(self) -> None:
        dif = self.stack.pop()
        if dif < 0:
            self.mini = self.mini - dif

    def top(self) -> int:
        dif = self.stack[-1]
        if dif > 0:
            return self.mini + dif
        else:
            return self.mini

    def getMin(self) -> int:
        return self.mini
