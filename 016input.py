# 7-1 Rental Car

car = input("What kind of car would you like? ")
print("Let me see if I can find you a " + car + ".")

# 7-2 Restaurant Setting

group = input("How many people are in your party?")
group = int(group)

if group >= 8:
    print("\nYou'll have to wait for a table.")
else:
    print("\nYour table is ready.")

# 7-3 Multiples of Ten

number = input("Enter a number, and I'll tell you if it is divisible by 10.")
number = int(number)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is divisible by 10.")
else:
    print("\nThe number " + str(number) + " is not divisible by 10.")