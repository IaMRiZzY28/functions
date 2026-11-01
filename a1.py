def greet_customer():
    print("Welcome to the Lemonade Stand!")
    print("Fresh lemonade, made just for you.")


greet_customer()

price_per_cup = float(input("Enter the price per cup in dollars: "))
cups_sold = int(input("Enter the number of cups sold: "))


def calculate_total(price, cups):
    total = price * cups
    return total

total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)
print("Total Cost:", rounded_total)

amount_paid = float(input("Enter the amount paid by the customer in dollars: "))

def calculate_change(total, paid):
    change = paid - total
    return change

change_due = calculate_change(rounded_total, amount_paid)
rounded_change  = round(change_due, 2)

def thank_you_message(cups):
    if cups >= 5:
        return "Thank you for your gigamax purchase! Enjoy your lemonadessssssssssssssssssss!"
    else:
        return "Thank you for your tiny purchase! you poor Enjoy your lemonade!"

closing_message = thank_you_message(cups_sold)

print("")
print(" ============= lemonade Stand Receipt ============= ")
print("price per cup: $", price_per_cup)
print("cups sold:", cups_sold)
print("total cost: $", rounded_total)
print("amount paid: $", amount_paid)
print("change due: $", rounded_change)
print(closing_message)
print("==================================================")