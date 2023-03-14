# PROJECT ROADMAP

## Fact Sheet

|Project|De Ars Aedifico|
|:---|:---|
|Project Release|0.0|
|Project Status|Development|
|Document version|0.1|
|Document status|Draft|
|Document date|2023-03-14|
|Author|@tanancuit06|
|Developer|@tanancuit06|
|Programming Languages|Python, C++|

## Objectives and goals

- Create a free open source toolset that performs and validates complex structural engineering calculations easily.
- It is called toolset as the idea is to make the software modular. This would enable the addition/modification/deletion of features easier and would minimize the risks of inadvertently breaking up the structure of the software.
- A toolset that can be used as an alternative and/or complement to paid modeling software.

## Releases and milestones

### Release 1.0

- Name: Statics 
- Estimated date: June 30, 2023
- Main modules:
   1. Structural Classes: file including the classes where the objects used to model will come from.
   2. Particle Statics
   3. Centroids and Gravity Centers
   4. Determined Trusses
   5. Determined Beams
   6. Cables
   7. Rigid Bodies
   8. Friction

### Release 1.1

- Name: Vectorial Mechanics
- Estimated date: December 31, 2023
- Main modules:
   1. Statics Release 1.0
   2. Motion and Kinetics of Particles
   3. Motion and Kinetics of Bodies
   4. Mechanical Vibrations

### Release 1.2

- Name: Structural Analysis
- Estimated date: December 31, 2024
- Main modules:
   1. Releases 1.0 and 1.1
   2. Slope-Deflection Analysis
   3. Matrix Analysis

### Release 1.3

- Name: Structural Design
- Estimated date: TBD
- Main modules: TBD

### Release 2.0

Release 2.0 is thought to be an implementation of Release 1.0 in C++ to achieve greater efficiency and include a polished GUI.

- Name: CppStatics
- Estimated date: TBD
- Main modules: the same as Release 1.0

### Other

The next releases, along the lines of Release 1.x and 2.x, will further enhance the capabilities of the toolset. The idea is to achieve the following objectives:

- Integration with matrix algebra libraries/packages.
- Integration with mesh generators.
- Creation of entities by using a GUI.
- Finite Element Analyses (FEA).
- Integration with post-processing software such as Paraview.
- Export models in other formats to allow being loaded in software such as FreeCAD.
- Etc...

The inclusion of these features might cause severe changes to the basic structure of the software, although common sense would that it is best to address these at the beginning to avoid major changes later, they are left at last as their development requires much more complex calculations and also deep understanding and knowledge of numerical methods, structural engineering and software development from the developer so it might be worth to develop these features as a separate toolset/application.

## Main Features

The main features are defined according to any of the two principal release branches.

### Release 1.x

1. It is written in Python to allow faster development and testing.
2. It uses the terminal rather than a GUI due to the same reasons stated above.
3. Most of scripts are imported to other scripts where needed, working as modules.
4. There is going to be a principal script, Structural_Classes.py, where classes used by all scripts are defined.
5. There is a main and a function script for each module, this means the main script will run as a program that allows to select several options which are functions included into the function script.

### Release 2.x

1. It will be likely written in C++.
2. It will include a GUI, probably derived from wxWidgets or GTK.
3. The scripts are going to be likely converted to header files in C++.
4. It will have the ability to use templates to load a model without having to add nodes, forces and other objects one by one. 

## Dependencies

### Release 1.0

- Python packages:
  - math
  - matplotlib
  - numpy

## Risks

TBD

## License

The current license is MPL-2.0 License, this is most likely temporary while a definitive license is chosen. The idea is to keep the software free and open source.