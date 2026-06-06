
def taxCalc(money):
    tax = 0
    initMoney = money
    if money >= 300000:
        money -= 300000
        if money >= 200000:
            money -= 200000
            if money >= 250000:
                money -= 250000
                if money >= 250000:
                    money -= 250000
                    if money:
                        tax+= money * 0.3
                    tax += 250000 * 0.1
                tax += 250000 * 0.075 
            tax += 200000 * 0.05
        tax += 300000 * 0
    return tax if initMoney > 0 else "You can't have less than ₹0." if initMoney < 0 else "You can't calculate for ₹0" 
while True:
    try:
        input_money = int(input("Enter an amount to calcute tax: ₹"))
        print()
        try:
            if taxCalc(input_money) == float(taxCalc(input_money)):
                print(f"The tax on the money is: ₹{taxCalc(input_money)}")
                print(f"And the total amount of money with tax is: ₹{taxCalc(input_money)+(input_money)}")
                print()
        except ValueError:
            print(taxCalc(input_money))
            print()
            continue
        break
    except ValueError:
        print("\nYou can't have text or symbol in the number.\n")
        continue
    