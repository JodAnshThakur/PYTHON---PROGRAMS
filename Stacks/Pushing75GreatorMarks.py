R = {"Om":76, "JAI" : 45, "BOB": 89, "ALI":65, "ANU":90,"TOM" : 82}

def Push(s,N):
    s.append(N)

def Pop(st):
    return st.pop()

st =[]
for i in R:
    if R[i]>75:
        Push(st,i)

while True :
    if st!= []:
        print(Pop(st))
    else :
        break
