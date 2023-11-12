class MinStack:

    def __init__(self):
        self.values = []
        self.sortValues = None

    def push(self, val: int) -> None:
        self.values.append(val)
        if self.sortValues is None:
            self.sortValues = [val]
        else:
            self.sortValues.sort()

    def pop(self) -> None:
        removed_val = self.values[0]
        self.values = self.values[1:]
        if len(self.values) == 0:
            self.sortValues = None
        else:
            self.sortValues.remove(removed_val)

    def top(self) -> int:
        if self.values is not None:
            return self.sortValues[0]
        else:
            return 0

    def getMin(self) -> int:
        if self.sortValues is not None:
            return self.sortValues[0]
        else:
            return 0
