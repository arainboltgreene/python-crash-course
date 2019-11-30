#7-4

#prompt = "\nEnter desired pizza toppings."
#prompt += "\nEnter 'quit' when done."
#
#while True:
#    topping = input(prompt)
#
#    if topping == 'quit':
#        break
#    else:
#        print("I'll add " + topping + " to your pizza.")

#7-5
prompt = "\nWhat is your age?"
while True:
    age = input(prompt)

    if age == "quit":
        break
    elif age < '3':
        print("Your ticket is free.")
    elif age < '12':
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")