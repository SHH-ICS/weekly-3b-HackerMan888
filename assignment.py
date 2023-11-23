#Add the price of the pizza along with the price of the topping. 
print("Welcome to Chaarlie's Pizzas!")
# Collect the pizza size from the user
pizza_size = input("What size pizza do you want (Large or Extra-Large)? L / XL: ")
if pizza_size != 'L' and pizza_size != 'XL':
  print('Invalid Pizza size choice!')
  quit()

# Collect the number of toppings from the user
toppings_number = input("How much toppings do you want on your pizza? (1 - 4): ")
if toppings_number == '':
  print('Invalid input for toppings!')
  quit()
elif toppings_number != '1' and toppings_number != '2' and toppings_number != '3' and toppings_number != '4': 
  print('Invalid input for toppings!')
  quit()

# Calculate the pizza cost based on the size that the user asked for
pizza_cost = 0
if pizza_size == "L":
  pizza_cost = 6.00
  pizzaWord = 'Large'
elif pizza_size == "XL":
  pizza_cost = 10.00
  pizzaWord = 'Extra Large'

# Calculate the toppings cost based on the number that the user asked for
toppings_cost = 0
if toppings_number == '1':
  toppings_cost = 1
elif toppings_number == '2':
  toppings_cost = 1.75
elif toppings_number == '3':
  toppings_cost = 2.50
elif toppings_number == '4':
  toppings_cost = 3.35

# Calculate the cost of the order before tax
subtotal = pizza_cost + toppings_cost
  
#Then calculate the tax by multiplying the total number by 1.13
total = round((subtotal * 1.13), 2)
# Summarize the order for the user and tell them how much they owe

print("You ordered a", pizzaWord, "pizza with", toppings_number, "toppings", "and your total is", total)
print("Your pizza will be ready in 25 minutes!")
