#problem 9
#olivia g 11/2/20
#setting constants - amount of points for each scoring method
TRY = 5
CONV = 2
PEN = 3
DROP = 3
#input - how many tries, conversions, etc.
try_num = int(input("How many tries did the team score this season? "))
conv_num = int(input("How many conversions did the team score this season? "))
pen_num = int(input("How many penalties did the team score this season? "))
drop_num = int(input("How many drop kicks did the team score this season? "))
#process - calculating the amount of points
try_points = try_num * TRY
conv_points = conv_num * CONV
pen_points = pen_num * PEN
drop_points = drop_num * DROP
total_points = try_points + conv_points + pen_points + drop_points
#output - printing individual point numbers and total points
print("----------------------")
print("Season try points ({} points): {}".format(TRY, try_points))
print("Season conversion points ({} points): {}".format(CONV, conv_points))
print("Season penalty points ({} points): {}".format(PEN, pen_points))
print("Season drop kick points ({} points): {}".format(DROP, drop_points))
print("Total season points: {}".format(total_points))
