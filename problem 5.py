#problem 5
#olivia g 10/2/20
import math
PI = math.pi
rad = float(input("Radius of the wheel in cm: "))
rot = float(input("Number of rotations: "))
diam = rad * 2
circ = PI * diam
dist = circ * rot
print("Distance travelled: {:.2f}cm".format(dist))
