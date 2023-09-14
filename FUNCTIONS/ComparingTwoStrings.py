def CompareStrings(a,b):
    if (len(a) == len(b)):
      for i  in range(len(a)):
        if a[i] != b[i] :
         return False
      else :
         return True
    else :
        return False
f = CompareStrings("Ansh", "Ansh")
if f==True :
   print("Strings are same")
else :
   print("Strings are different")


