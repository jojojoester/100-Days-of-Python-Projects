#Welcoming the user to our Tip Calculator
#The main objectives of this code is to find the amount each person has to pay as per the number of the person.
print("Welcome to Tip Calculator")
#asking the user about the total bill
bill = float(input("What was the total bill? $"))
#asking the user what percentage of tip they would like to give.
tip = int(input("What precentage of tip would you like to give? 10, 11 or 15 :"))
#after getting both total amount of bill and tip that the user would like to give, 
people = int(input("How many people to split the bill?"))
#asking the number of people
tip_as_percent = tip / 100
#first, finding the tip as percent. Initially, the tip is on percentage so dividing it by 100 to find the tip amount.
total_tip_amount = bill * tip_as_percent
#finding the total_tip_amount by multiplying it to the bill
total_bill = bill + total_tip_amount
#finding the total bill by adding the total_tip_amount to the bill.
bill_per_person = total_bill / people
#now finding the number of people and dividing the bill as per the number of the person
total_amount = round(bill_per_person, 2)
#rounding the bill_per_person amount with only two decimal value after the decimal point and
#storing the final amount to total_amount variable and finally printing it.
print(f"Each person should pay ${total_amount}") 