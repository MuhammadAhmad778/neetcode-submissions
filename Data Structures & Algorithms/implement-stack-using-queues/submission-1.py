class MyStack:

    def __init__(self):
        self.arr1=[]

        

    def push(self, x: int) -> None:
        self.arr1.append(x)
        

    def pop(self) -> int:
        return self.arr1.pop()
        

    def top(self) -> int:
        return self.arr1[-1]
        

    def empty(self) -> bool:
       return len(self.arr1)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()