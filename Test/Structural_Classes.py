# ------------------------------------------------------------------------
# Structural_Classes.py
# 
# Description: 
# This module contains the declaration for the essential classes that are
# going to be used by all scripts.
#
# Author: tanancuit06
# Original date: 05/02/2023
# Last modified date: 12/02/2023
# ------------------------------------------------------------------------

class Node:
    # Instance attribute
    def __init__(self,node_id,x,y,z):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.z = z
        self.dict = {"Node_id": node_id, "x": x, "y": y, "z": z}


class Beam:
    # Instance attribute
    def __init__(self,beam_id,node_1,node_2):
        self.beam_id = beam_id
        self.node_1 = node_1
        self.node_2 = node_2
        self.dict = {"Beam_id": beam_id, "node_1": node_1, "node_2": node_2}

class Force:
    # Instance attribute
    def __init__(self,Force_id,Fx,Fy,Fz):
        self.Force_id = Force_id
        self.Fx = Fx
        self.Fy = Fy
        self.Fz = Fz
        self.dict = {"Force_id": Force_id, "Fx": Fx, "Fy": Fy, "z": Fz}

class Support:
    pass

class Material:
    pass

class Section:
    pass

class Constraint:
    pass

class Membrane:
    pass

class Plate:
    pass

class Shell:
    pass