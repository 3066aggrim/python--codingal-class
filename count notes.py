# Calculating toatal amount as input from user
Amount = int(input("please enter amount for withdraw:"))

# calculating the number of notes of different denominations
note1 = Amount//1000
note2 = (Amount % 1000)//100
note3 = ((Amount % 1000) % 100)//50
note4 = (((Amount % 1000) % 100) % 50)//20
note5 = ((((Amount % 1000) % 100) % 50) % 20)//10

print("notes of 1000", note1)
print("notes of 100 rupee", note2)
print("notes of 50 rupee", note3)
print("notes of rupee 20", note4)
print("notes of 10 rupee", note5)
