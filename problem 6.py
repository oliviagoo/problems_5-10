#olivia
#5/2/20

#declaring the constants
MAIN_PRICE = 12.5
DESSERT_PRICE = 6
DRINK_PRICE = 3.55

#getting input
order_main = int(input("How many mains did you order? "))
order_dessert = int(input("How many desserts did you order? "))
order_drink = int(input("How many drinks did you order? "))

#process - calculation
main_cost = order_main * MAIN_PRICE
dessert_cost = order_dessert * DESSERT_PRICE
drink_cost = order_drink * DRINK_PRICE
total_cost = main_cost + dessert_cost + drink_cost

#output
print("--------------------")
print("{} mains at ${:.2f} is ${:.2f}".format(order_main, MAIN_PRICE, main_cost))
print("{} desserts at ${:.2f} is ${:.2f}".format(order_dessert, DESSERT_PRICE, dessert_cost))
print("{} drinks at ${:.2f} is ${:.2f}".format(order_drink, DRINK_PRICE, drink_cost))
print("Price of meal: ${:.2f}".format(total_cost))
