#Printing the project name
print("Bill Split Calculator")

bill_amount = float(input("Enter Bill Amount: "))
tip_percentage = float(input("Enter Tip Percentage: "))
num_of_people = int(input("Enter Number of People: "))

tip_amount = (tip_percentage / 100) * bill_amount
total_amount_paid = bill_amount + tip_amount
amount_per_person = total_amount_paid / num_of_people

print(f"Total Amount Paid (including tip): {total_amount_paid}")
print(f"Each person pays: {amount_per_person}")


