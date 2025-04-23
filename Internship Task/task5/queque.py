from collections import deque

class Queue:
    def __init__(self):
        self.queue=deque()

    def isempty(self):
        return len(self.queue)==0

    def push(self,item):
        self.queue.append((item))

    def pop(self):
        if self.isempty():
            print("there is no element so can't perform pop operations")
        else:
            removed=self.queue.popleft()
            return removed
    def peek(self):
        if self.isempty():
            print("there is no element")
        else:
            return self.queue[-1]
    def display(self):
        print(list(self.queue))
q=Queue()
print(q.isempty())
q.push(10)
q.push(20)
q.push(30)
q.display()
print(q.isempty())
print(q.peek())
q.pop()
q.pop()
q.display()


