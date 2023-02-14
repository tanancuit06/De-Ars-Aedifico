#---------------------------------------------------------------------------
# Centroid_2D.py
# 
# Description:
# This script provides the mathematical means to calculate the geometric
# centroid of any 2D object. It is thought to use the Gauss's Area Formula 
# to calculate the simple polygon area.
# 
# Final phase 
# Input: option
# Method: Centroid 2D functions (Centroid_2D_func.py)
# Output: area and centroid of polygon
#
# Author: tanancuit06
# Original date: 05/02/2023
# Last modified date: 14/02/2023
#---------------------------------------------------------------------------

# Import lines
import Centroid_2D_func

# Variables initialization
node_list = []
node_list_x = []
node_list_y = []

while(True):
    print("")
    print("Welcome. This script calculates the area of a polygon. This can be used to calculate centroids. \n", 
    "Your options are: \n",
    "A. Add a node to create a polygon. \n",
    "C. Calculate the area and centroid of the polygon created by the nodes. \n",
    "D. Draw and print the polygon. \n",
    "P. Print the current node list \n",
    "R. Clear an existing polygon. \n",
    "Q. Quit \n")
    option = input("Option: ")

    if option in ("A","a"):
        node_id = input("Type the id of your node: ")
        x_coord = float(input("Type the x-coordinate of your node: "))
        y_coord = float(input("Type the y-coordinate of your node: "))
        z_coord = float(input("Type the z-coordinate of your node: "))

        # Node creation
        Centroid_2D_func.add_node(node_list,node_id,x_coord,y_coord,z_coord)

    elif option in ("C","c"):

        # Polygon coordinates arrays creation

        Centroid_2D_func.create_node_lists(node_list,node_list_x, node_list_y)

        # Gauss's Area Formula
        polygon_area = Centroid_2D_func.gauss_area_formula(node_list_x, node_list_y)

        # Centroid formulas
        node_list_x.append(node_list_x[0])
        node_list_y.append(node_list_y[0])

        Cx, Cy = Centroid_2D_func.centroid_coordinates(polygon_area, node_list_x, node_list_y)

        node_list_x.pop()
        node_list_y.pop()

    elif option in ("D","d"):
        # Polygon drawing
        node_list_x.append(node_list_x[0])
        node_list_y.append(node_list_y[0])

        Centroid_2D_func.draw_polygon(node_list_x, node_list_y, Cx, Cy)

        node_list_x.pop()
        node_list_y.pop()

    elif option in ("P","p"):
        print(node_list)

    elif option in ("R","r"):
        node_list.clear()
        node_list_x.clear()
        node_list_y.clear()
        print("node_list is now empty:", node_list)
        print("node_list_x is now empty:", node_list_x)
        print("node_list_y is now empty:", node_list_y)

    elif option in ("Q","q"):
        break

    else:
        print("Invalid option, select again.")
        continue

del node_list, node_list_x, node_list_y