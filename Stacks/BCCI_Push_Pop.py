#Pushing the names of the players who had a score of more then 49.
def PUSH(st,name):
    st.append(name)

#Function to Pop the elements stored during pushing..
def POP(st) :
    return st.pop()

# checking conditions for Pushing
SCORE = {"KAPIL":40,"SACHIN" :55,"SAURAV" :80,"RAHUL" :35,"YUVRAJ" :110}
st =[]
for i  in SCORE:
    if SCORE[i]>49:
        PUSH(st,i)
print(st)

# #Checking conditions for poping the elements.
while True:
    if st != []:
        print(POP(st))
    



