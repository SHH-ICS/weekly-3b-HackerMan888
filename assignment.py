#Add the price of the pizza along with the price of the topping. 

# Collect the pizza size from the user
pizza_size = input("What size pizza do you want? L / XL")

# Collect the number of toppings from the user
toppings_number = input("How much toppings do you want on your pizza? 1 / 2 / 3 / 4")

# Calculate the pizza cost based on the size that the user asked for
if pizza_size == "L":
  pizza_cost = 6.00
elif pizza_size == "XL:
  pizza_cost = 10.00

# Calculate the toppings cost based on the number that the user asked for

if toppings_number == "1":
  toppings_cost = 1
elif toppings_number == "2":
  toppings_cost == 1.75
elif toppings_number == "3":
  toppings_cost = 2.50
elif toppings_number == "4":
  toppings_cost = 3.35

# Calculate the cost of the order before tax
subtotal = pizza_cost + toppings_number
  
#Then calculate the tax by multiplying the total number by 1.13
subtotal * 1.13

# Summarize the order for the user and tell them how much they owe

print("You ordered a", pizza_size, "with", toppings_number)
