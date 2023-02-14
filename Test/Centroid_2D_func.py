#---------------------------------------------------------------------------
# Centroid_2D_func.py
# 
# Description:
# This script provides the functions to make Centroid_2D.py work. 
# Centroid_2D.py is a script that provides mathematical means to calculate 
# the geometric centroid of any 2D object. It is thought to use the Gauss's 
# Area Formula to calculate the simple polygon area.
# 
# Phase 1: Area calculation (05/02/2023)
# Input: nodes coordinates
# Method: Gauss's Area Formula
# Output: area value
# 
# Phase 2: Centroid calculation (12/02/2023)
# Input: nodes coordinates, area
# Method: centroid of polygon formulas
# Output: centroid coordinates
#
# Author: tanancuit06
# Original date: 05/02/2023
# Last modified date: 13/02/2023
#---------------------------------------------------------------------------

# Import lines
import Structural_Classes
import matplotlib.pyplot as plt
import numpy as np

# Functions
def add_node(node_list,node_id,x,y,z):
    new_node = Structural_Classes.Node(node_id,x,y,z)
    node_list.append(new_node.dict)
    del new_node
    return node_list

def create_node_lists(node_list,node_list_x, node_list_y):
    for i in range(len(node_list)):
        node_list_x.append(node_list[i]["x"])
        node_list_y.append(node_list[i]["y"])
    print("Node list of x-coordinates: ", node_list_x, "\n" + "Node list of y-coordinates: ", node_list_y)
    return node_list_x, node_list_y

def draw_polygon(node_list_x, node_list_y,Cx,Cy):
    plt.plot(node_list_x,node_list_y)
    plt.plot(Cx,Cy,'r^')
    plt.title('Area of polygon')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.show()

def gauss_area_formula(node_list_x, node_list_y):
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
    return polygon_area

def centroid_coordinates(polygon_area, node_list_x, node_list_y):
    Cx = 0
    for i in range(len(node_list_x)-1):
        Cx += (node_list_x[i] + node_list_x[i+1]) * (node_list_x[i]*node_list_y[i+1] - node_list_x[i+1]*node_list_y[i])
    Cx = (1/(6*polygon_area))*abs(Cx)
    
    Cy = 0
    for i in range(len(node_list_y)-1):
        Cy += (node_list_y[i] + node_list_y[i+1]) * (node_list_x[i]*node_list_y[i+1] - node_list_x[i+1]*node_list_y[i])
    Cy = (1/(6*polygon_area))*abs(Cy)

    print("Centroid x-coordinate: ", Cx, "\n" + "Centroid y-coordinate: ", Cy)

    return Cx, Cy
