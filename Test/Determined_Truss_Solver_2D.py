#---------------------------------------------------------------------------
# Determined_Truss_Solver_2D.py
# 
# Description:
# This script provides a determined truss solver so the user can find 
# the support reactions when a truss is subjected so several forces on 
# its nodes.
#
# Author: tanancuit06
# Original date: 05/02/2023
# Last modified date: 05/02/2023
#---------------------------------------------------------------------------

import Structural_Classes

node1 = Structural_Classes.Node("01",1,2,3)
print("Node ", str(node1.node_id), " created: \
(",node1.x, ",", node1.y, ",",node1.z, ")")
name = node1.node_id
del node1
print("Node ", name, " deleted")