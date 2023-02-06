#---------------------------------------------------------------------------
# Centroid_2D.py
# 
# This script provides the mathematical means to calculate the geometric
# centroid of any 2D object. It is thought to use the Gauss's Area Formula 
# to calculate the simple polygon area.
# 
# Phase 1: Area calculation
# Input: nodes coordinates
# Gauss's Area Formula
# Output: area value
#---------------------------------------------------------------------------

# Import lines
import Structural_Classes as struct_clss
import numpy as np
import matplotlib.pyplot as plt

# Node creation
node1 = struct_clss.Node('A',1,1,0)
node2 = struct_clss.Node('B',2,4,0)
node3 = struct_clss.Node('C',5,5,0)
node4 = struct_clss.Node('D',4,2,0)

# Polygon drawing
plt.plot([node1.x,node2.x,node3.x,node4.x,node1.x],
[node1.y,node2.y,node3.y,node4.y,node1.y])
plt.ylabel('Area of polygon')
plt.show()

# Arrays creation
x_array = np.array([node1.x,node2.x,node3.x,node4.x])
y_array = np.array([node1.y,node2.y,node3.y,node4.y])

# Gauss's Area Formula
sum_x = 0
for i in range(0,len(x_array)-1):
    sum_x += x_array[i]*y_array[i+1]
    print(sum_x)

sum_y = 0
for i in range(0,len(y_array)-1):
    sum_y += x_array[i+1]*y_array[i]
    print(sum_y)

prod_1 = x_array[len(x_array)-1]*y_array[0]
prod_2 = x_array[0]*y_array[len(y_array)-1]

polygon_area = 0.5*np.abs(sum_x + prod_1 - sum_y - prod_2)
print("Polygon area = ", polygon_area)

