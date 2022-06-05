print("Welcome to m's tip calculator!")
total_bill = float(input("How much is your total bill? \n₦"))
answer = input(
    "In lagos the standard tip is 10%, would you like to use the standard or not? [yes/no]\n")
if answer == "yes":
    percent = 10
else:
    percent = int(input("Please enter the percentage you would like to use: "))


no_of_people = int(input("How many people are spliting the bill? "))


final_percent = (percent/100) + 1
tip_per_person = "{:.2f}".format(total_bill/no_of_people * final_percent)

if no_of_people == 1:
    print(f"You are to pay ₦{tip_per_person}")
else:
    print(f"You are each to pay N{tip_per_person}")
