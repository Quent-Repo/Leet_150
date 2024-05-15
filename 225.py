def __init__(self):
    self.q = deque()
def push(self, x):
    self.q.append(x)

def pop():
    for i in range(len(self.q)-1):
        self.push(self.q.popleft())
    return self.q.popleft()

def top(self):
    for i in range(len(self.q)-1):
        self.push(self.q.popleft())
    res = self.q[0]
    self.push(self.q.popleft())
    return res

def empty(self):
    return len(self.q) == 0
