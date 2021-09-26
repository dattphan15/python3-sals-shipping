from decimal import Decimal
weight = 41.5


# Ground Shipping
cost_ground = 0

if weight <= 2:
  cost_ground = (weight * 1.50) + 20
elif (weight > 2) and (weight <= 6):
  cost_ground = (weight * 3.00) + 20
elif (weight > 6) and (weight <= 10):
  cost_ground = (weight * 4.00) + 20
else:
  cost_ground = (weight * 4.75) + 20
# Convert to decimal
cost_ground = Decimal(cost_ground)


# Ground Shipping Premium
cost_ground_premium = 125.00
# convert to decimal
cost_ground_premium = Decimal(cost_ground_premium)


# Drone Shipping
cost_drone_shipping = 0

if weight <= 2:
  cost_drone_shipping = (weight * 4.50)
elif (weight > 2) and (weight <= 6):
  cost_drone_shipping = (weight * 9.00)
elif (weight > 6) and (weight <= 10):
  cost_drone_shipping = (weight * 12.00)
else:
  cost_drone_shipping = (weight * 14.25)
# convert to decimal
cost_drone_shipping = Decimal(cost_drone_shipping)

print(""" 
Based on a package weight of {weight}lb
""".format(weight = str(weight)))
print("Ground Shipping: $" + str(round(cost_ground, 2)))
print("Ground Shipping Premium: $" + str(round(cost_ground_premium, 2)))
print("Ground Drone Shipping: $" + str(round(cost_drone_shipping, 2)))
