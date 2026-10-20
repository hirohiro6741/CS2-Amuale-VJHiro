# Electricity Bill Calculator
RATE = 12.90

while True:
    name = input("Enter customer name: ")
    if name == "":
        print("Please input a name.")
    else:
        break
while True:
    previous = float(input("Enter previous meter reading: "))
    if previous <= 0 or previous == "":
        print("Please input a reading.")
    else:
        break
while True:
    current = float(input("Enter current meter reading: "))
    if previous >= current:
        print("Your current reading should be atleast the previous reading")
    else:
        break

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
