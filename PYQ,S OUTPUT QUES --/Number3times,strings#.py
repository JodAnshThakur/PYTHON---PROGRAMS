#if element is a number print it 3 times and if it is a word then print that word ending with# as finaml output

def op(L):
    for i in L:
        if i.isdigit():
            print(i*3)
        else :
            print(i, '#')
op([10,"ansh",20,"OpBolte"])