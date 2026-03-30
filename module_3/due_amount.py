total_bill = int(input("please enter total bill amount: "))
paid_money = int(input("please enter custumers paid money: "))


if total_bill == paid_money:
    print("transaction complete no due amount")

elif total_bill > paid_money:
    due_amount = total_bill-paid_money
    print("due amount is: ", due_amount)

elif paid_money > total_bill:
    tip = paid_money-total_bill
    print("thanks for the tip have a good day😊😊 your tip is", tip)
