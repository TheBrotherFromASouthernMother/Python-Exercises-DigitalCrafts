bill = float(input("Total Bill Amount? "))
qualService = str(input("Level of service(good, fair, bad)? ")).upper() 
numberOfPatrons = int(input("How Many in your party? "))

tipAmount = 0
if qualService == "GOOD":
    tipAmount = 0.20
elif qualService == "FAIR":
    tipAmount = 0.15
else:
    tipAmount = 0.10

totalBill = bill + (bill * tipAmount)
individualBill = totalBill / numberOfPatrons

print("Total Amount: ${:.2f}".format(totalBill))
print("Amount per person: ${:.2f}".format(individualBill))