def box_vol(len,wid,hgt):
    volume = len*wid*hgt
    print(volume, "cubic cm")
len = int(input("Enter the lenght of the cube in cm :"))
wid = int(input("Enter the width of the box in cm:"))
hgt = int(input("Enter the height of the box in cm:"))
box_vol(len,wid,hgt)