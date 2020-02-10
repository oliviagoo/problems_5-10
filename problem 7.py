#problem 7
#olivia g 10/2/20
#setting the constants - track prices
SHORT = 1.79
MEDIUM = 2.5
LONG = 4.5
#input - balance, and how many tracks were bought
bal = float(input("What is your initial balance? "))
purch_s = int(input("How many short tracks did you buy? "))
purch_m = int(input("How many medium tracks did you buy? "))
purch_l = int(input("How many long tracks did you buy? "))
#process - calculations
s_cost = purch_s * SHORT
m_cost = purch_m * MEDIUM
l_cost = purch_l * LONG
tot_cost = s_cost + m_cost + l_cost
newbal = bal - tot_cost
#output - balance updates and costs
print("------------------")
print("Initial balance: ${:.2f}".format(bal))
print("Purchased {} short tracks at ${:.2f}".format(purch_s, SHORT))
print("Purchased {} medium tracks at ${:.2f}".format(purch_m, MEDIUM))
print("Purchased {} long tracks at ${:.2f}".format(purch_l, LONG))
print("Final balance: ${:.2f}".format(newbal))
