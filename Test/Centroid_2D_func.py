#---------------------------------------------------------------------------
# Centroid_2D_func.py
# 
# Description:
# This script provides the functions to make Centroid_2D.py work. 
# Centroid_2D.py is a script that provides mathematical means to calculate 
# the geometric centroid of any 2D object. It is thought to use the Gauss's 
# Area Formula to calculate the simple polygon area.
# 
# Phase 1: Area calculation
# Input: nodes coordinates
# Gauss's Area Formula
# Output: area value
#
# Author: tanancuit06
# Original date: 08/02/2023
# Last modified date: 12/02/2023
#---------------------------------------------------------------------------

# Import lines
import Structural_Classes as struct_clss

# Functions
def add_node(node_list,node_id,x,y,z):
    new_node = struct_clss.Node(node_id,x,y,z)
    node_list.append(new_node.dict)
    del new_node
    return node_list