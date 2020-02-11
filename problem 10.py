#problem 10
#olivia g 11/2/20
#setting constants - the cost rate and the weight of punnets etc.
RATE = 5
PUN = 0.25
BOX = 1.5
BUCK = 7
#input - how many punnets, etc.
pun_num = int(input("How many punnets did you pick? "))
box_num = int(input("How many boxes did you pick? "))
buck_num = int(input("How many buckets did you pick? "))
#process - calculating the weight and price
pun_weight = pun_num * PUN
box_weight = box_num * BOX
buck_weight = buck_num * BUCK
total_weight = pun_weight + box_weight + buck_weight
total_price = total_weight * RATE
#output - outputting the weights and the total price
print("-----------------")
print("Total punnet weight: {:.1f} kg".format(pun_weight))
print("Total box weight: {:.1f} kg".format(box_weight))
print("Total bucket weight: {:.1f} kg".format(buck_weight))
print("Total berry weight: {:.1f} kg".format(total_weight))
print("Price to charge: ${:.2f}".format(total_price))
