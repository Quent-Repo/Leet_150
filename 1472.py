def __init__(self,homepage):
    self.i=0
    self.len=1
    self.history = [homepage]

def visit(self, url):
    if len(self.history) < self.i +2:
        self.history.append(url)
    else:
        self.history[self.i+1]=url
    self.i+=1
    self.len = self.i +1

def back(self,step):
    self.i=max(self.i -steps,0)
    return self.history[self,i]

def forward(self,steps):
    self.i=min(self.i +steps, self.len-1)
    return self.history[self.i]
