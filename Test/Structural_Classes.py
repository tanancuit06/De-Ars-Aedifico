# ----------------------------------------------------------
# Structural_Classes.py
# 
# 
# ----------------------------------------------------------

class Node:
    # Instance attribute
    def __init__(self,node_id,x,y,z):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.z = z

class Beam:
    # Instance attribute
    def __init__(self,beam_id,node_1,node_2):
        self.beam_id = beam_id
        self.node_1 = node_1
        self.node_2 = node_2

class Force:
    pass

class Support:
    pass

class Constraint:
    pass

class Membrane:
    pass

class Plate:
    pass

class Shell:
    pass