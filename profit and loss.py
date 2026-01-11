costprice = int(input("enter the cp :"))
sellingprice = int(input("enter the sp:"))

if (sellingprice > costprice):
    print("it is a profit")
    profit = sellingprice - costprice
    print("profit", profit)

if (costprice > sellingprice):
    print("it is loss")
    loss = costprice-sellingprice
    print("loss", loss)
