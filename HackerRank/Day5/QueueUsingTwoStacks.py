# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


class Queue():
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

    def print_(self):
        if self.outstack:
            print(self.outstack[-1])
        else:
            print(self.instack[0])

q = Queue()

for _ in range(int(input())):
    cmd = input()
    if cmd[0] == "1":
        q.enqueue(int(cmd.split(" ")[1]))
    elif cmd[0] == "2":
        q.dequeue()
    else:
        q.print_()
