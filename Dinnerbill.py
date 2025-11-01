bill_amt = float(input("Bill amount"))
tip = float(input("Tip percentage"))
friends = float(input("Total no.of friends"))
tip_amount= (bill_amt/100)*tip
total_bill = bill_amt+tip_amount
total_amount_perhead = round((total_bill)/friends)


#h = (x+e)/z
#print(f"Total bill after adding {total_bill} friends and per head cost is {total_amount_perhead:.2f}") -- to round the col use :.2f
print(f"Total bill after adding {total_bill} friends and per head cost is {total_amount_perhead}")

