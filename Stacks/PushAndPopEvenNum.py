N = [12,13,34,56,21,79,98,22,35,38]

def Push(fn,N):
    fn.append(N)  

def Pop(fn):
    return fn.pop()

fn = []
for i in N:
    if i % 2 == 0:
        Push(fn,i)
print(fn)

while True:
    if fn != []:
        print(Pop(fn))
