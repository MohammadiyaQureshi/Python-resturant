# 🧾 Python Restaurant Ordering Program - Enhanced

menu = { 
    'pizza': 2000,
    'burger': 500,
    'salad': 300,
    'coffee': 800
}

print("\n🌟 Welcome to Our Python Restaurant! 🌟\n")
print("📋 MENU:")
for item, price in menu.items():
    print(f"🍽 {item.capitalize()} - Rs. {price}")

order_total = 0
orders = {}

while True:
    item = input("\nEnter the name of one item you want to order: ").lower()
    
    if item in menu:
        quantity = input(f"How many {item.capitalize()}(s) would you like? ")
        if quantity.isdigit():
            quantity = int(quantity)
            order_total += menu[item] * quantity

            if item in orders:
                orders[item] += quantity
            else:
                orders[item] = quantity

            print(f"✅ {quantity} x {item.capitalize()} added to your order.")
        else:
            print("❌ Please enter a valid quantity.")
    else:
        print(f"⚠️ Sorry, {item.capitalize()} is not available.")

    another = input("\nWould you like to order anything else? (yes/no): ").lower()
    if another != "yes":
        break

# 🧾 Final Bill
print("\n==============================")
print("🧾 Final Bill Summary:")
for item, qty in orders.items():
    price = menu[item] * qty
    print(f"{item.capitalize()} x {qty} = Rs. {price}")
print("------------------------------")
print(f"💰 Total Amount to Pay: Rs. {order_total}")
print("==============================")
print("🙏 Thank you for ordering from our Python Restaurant!")
