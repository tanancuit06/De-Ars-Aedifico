#---------------------------------------------------------------------------
# Determined_Truss_Solver_2D.py
# 
# This script provides a determined truss solver so the user can find 
# the support reactions when a truss is subjected so several forces on 
# its nodes.
#---------------------------------------------------------------------------

import Structural_Classes

node1 = Structural_Classes.Node("01",1,2,3)
print("Node ", str(node1.node_id), " created: \
(",node1.x, ",", node1.y, ",",node1.z, ")")
name = node1.node_id
del node1
print("Node ", name, " deleted")