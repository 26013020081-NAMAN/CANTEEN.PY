# COLLEGE CANTEEN MANAGEMENT SYSTEM
# FY B.Tech Python Mini Project

from datetime import datetime

# Food menu: item number -> [item name, price]
menu = {
    1: ["Sandwich", 50],
    2: ["Burger", 80],
    3: ["Pizza", 120],
    4: ["Tea", 15],
    5: ["Coffee", 30],
    6: ["Cold Drink", 40],
    7: ["Pasta", 100]
}

cart = []
total = 0

print("=" * 40)
print("     COLLEGE CANTEEN MANAGEMENT")
print("=" * 40)

print("\n--------- FOOD MENU ---------")
for number, item in menu.items():
    print(number, ".", item[0], "- Rs.", item[1])

print("\nEnter 0 to finish your order.")

# Take customer orders
while True:
    try:
        choice = int(input("\nEnter item number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 0:
        break

    if choice not in menu:
        print("Invalid choice! Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid quantity.")
        continue

    if quantity <= 0:
        print("Please enter a quantity greater than zero.")
        continue

    name = menu[choice][0]
    price = menu[choice][1]
    amount = price * quantity
    total += amount

    cart.append([name, price, quantity, amount])
    print(name, "added successfully!")

# Calculate discount
discount = 0
if total >= 500:
    discount = total * 0.10

final_amount = total - discount

# Display bill
print("\n" + "=" * 40)
print("              FINAL BILL")
print("=" * 40)
print("Date:", datetime.now().strftime("%d-%m-%Y %H:%M"))
print("-" * 40)

if not cart:
    print("No items were ordered.")
else:
    for item in cart:
        print(item[0], "x", item[2], "= Rs.", item[3])

print("-" * 40)
print("Total Amount: Rs.", total)
print("Discount: Rs.", discount)
print("Final Amount: Rs.", final_amount)
print("=" * 40)
print("   THANK YOU! VISIT AGAIN!")
print("=" * 40)

# Save bill details in a text file
with open("canteen_bill.txt", "a", encoding="utf-8") as file:
    file.write("\nNEW BILL\n")
    file.write("Date: " + datetime.now().strftime("%d-%m-%Y %H:%M") + "\n")

    for item in cart:
        file.write(f"{item[0]} x {item[2]} = Rs. {item[3]}\n")

    file.write(f"Total: Rs. {total}\n")
    file.write(f"Discount: Rs. {discount}\n")
    file.write(f"Final Amount: Rs. {final_amount}\n")
    file.write("-" * 30 + "\n")

print("\nBill saved successfully in canteen_bill.txt")
