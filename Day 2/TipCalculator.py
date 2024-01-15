#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
total_people = input("How many people to split the bill? ")

split_bill_tip= float(total_bill) / int(total_people) * (int(tip)/100 + 1)




print(f"Each person should pay: ${round(split_bill_tip, 2)}" )

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
