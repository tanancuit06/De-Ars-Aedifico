#---------------------------------------------------------------------------
# Centroid_2D.py
# 
# Description:
# This script provides the mathematical means to calculate the geometric
# centroid of any 2D object. It is thought to use the Gauss's Area Formula 
# to calculate the simple polygon area.
# 
# Phase 1: Area calculation (05/02/2023)
# Input: nodes coordinates
# Method: Gauss's Area Formula
# Output: area value
# 
# Phase 2: Area calculation (12/02/2023)
# Input: nodes coordinates, area
# Method: centroid of polygon formulas
# Output: centroid coordinates
#
# Author: tanancuit06
# Original date: 05/02/2023
# Last modified date: 13/02/2023
#---------------------------------------------------------------------------

# Import lines
import Structural_Classes as struct_clss
import Centroid_2D_func
import numpy as np
import matplotlib.pyplot as plt

# Node creation
node_list = []
Centroid_2D_func.add_node(node_list,"0",1,1,0)
Centroid_2D_func.add_node(node_list,"0",2,4,0)
Centroid_2D_func.add_node(node_list,"0",5,5,0)
Centroid_2D_func.add_node(node_list,"0",4,2,0)

# Polygon coordinates arrays creation
node_list_x = []
node_list_y = []

for i in range(len(node_list)):
    node_list_x.append(node_list[i]["x"])
    node_list_y.append(node_list[i]["y"])

node_list_x.append(node_list_x[0])
node_list_y.append(node_list_y[0])

# Polygon drawing
plt.plot(node_list_x,node_list_y)
plt.title('Area of polygon')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

node_list_x.pop()
node_list_y.pop()

print("Node list of x coordinates: ", node_list_x, "\n" + "Node list of y coordinates: ", node_list_y)

# Gauss's Area Formula
sum_x = 0
for i in range(0,len(node_list_x)-1):
    sum_x += node_list_x[i]*node_list_y[i+1]

sum_y = 0
for i in range(0,len(node_list_y)-1):
    sum_y += node_list_x[i+1]*node_list_y[i]

prod_1 = node_list_x[len(node_list_x)-1]*node_list_y[0]
prod_2 = node_list_x[0]*node_list_y[len(node_list_y)-1]

polygon_area = 0.5*np.abs(sum_x + prod_1 - sum_y - prod_2)
print("Polygon area = ", polygon_area)

# Centroid formulas

node_list_x.append(node_list_x[0])
node_list_y.append(node_list_y[0])

Cx = 0
for i in range(len(node_list_x)-1):
    Cx += (node_list_x[i] + node_list_x[i+1]) * (node_list_x[i]*node_list_y[i+1] - node_list_x[i+1]*node_list_y[i])
Cx = (1/(6*polygon_area))*abs(Cx)

Cy = 0
for i in range(len(node_list_y)-1):
    Cy += (node_list_y[i] + node_list_y[i+1]) * (node_list_x[i]*node_list_y[i+1] - node_list_x[i+1]*node_list_y[i])
Cy = (1/(6*polygon_area))*abs(Cy)

print("Centroid x-coordinate: ", Cx, "\n" + "Centroid y-coordinate: ", Cy)

'''
# Program loop
while(True):
    print("Welcome. This script calculates the area of a polygon.",
    "This can be used to calculate centroids. \n", 
    "Your options are: \n",
    "A. Add a node to create a polygon. \n",
    "C. Calculate the area of the polygon created by the nodes. \n",
    "D. Draw and print the polygon. \n",
    "R. Clean an existing polygon. \n",
    "Q. Quit \n")
    option = input("Option: ")

'''