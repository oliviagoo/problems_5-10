#problem 5
#olivia g 10/2/20
#importing the math program to use pi
import math
#setting the PI constant
PI = math.pi
#input - radius and rotations
rad = float(input("Radius of the wheel in cm: "))
rot = float(input("Number of rotations: "))
#process - calculations
diam = rad * 2
circ = PI * diam
dist = circ * rot
#output - the dist. travelled
print("Distance travelled: {:.2f}cm".format(dist))
