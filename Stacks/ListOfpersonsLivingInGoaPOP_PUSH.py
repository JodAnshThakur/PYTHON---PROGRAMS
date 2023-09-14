#Pushing the elements of the list whose address is GOA.
def Push_Element(l_customer,status):
    for i in l_customer:
         if 'Goa' in i:
            status.append(i)
def Pop_element(status):
    for i in status:
        if i != []:
            print(status.pop())
        else:
         print("Stack Empty")

#Poping the value stored in the status Stack.
# def Pop_element(status):
#     for i in status :
#         if status != []:
#             print(status.pop())
#     else:
#         print("Stack empty")
status = []
l_customer = [['Gurudas','100000','Goa'],['Julee','526546','Mumbai'],['Murugan','655464','Coachin'],['Ashmit','12333','Goa'],]
Push_Element(l_customer,status)
print(status)
Pop_element(status)
# Pop_element(status)