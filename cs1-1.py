# Author: CRS 10/14/21
x1 = int(input("Input your first x value."))
y1 = int(input("Input your first y value."))
x2 = int(input("Input your second x value."))
y2 = int(input("Input your second y value."))
distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** .5
distance = str(distance)
print("Distance = " + distance)
