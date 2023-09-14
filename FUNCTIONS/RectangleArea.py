def RectangleArea(len,wid):
    area = len*wid
    return area
len = float(input(("Enter the length of the rectangle: ")))
wid = float(input(("Enter the width of the rectangle: ")))
area = RectangleArea(len,wid)
print(area)