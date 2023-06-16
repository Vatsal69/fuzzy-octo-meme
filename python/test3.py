number = 7
month = int(input("Enter the month of your birth: "))
day = int(input("Enter the day of your birth: "))

result = ((((((((number * month - 1) * 13 + day) + 3) * 11 - month) - day) / 10) + 11) / 100)

print("Your birthday is:", result)

#Trick Source
#             https://www.dr-mikes-math-games-for-kids.com/magical-calculator-birthday-math-trick.html
