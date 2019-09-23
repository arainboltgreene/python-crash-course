# 5-3 alien colors #1

alien_colors = ['green']

if 'green' in alien_colors:
    print("You just earned 5 points!")

if 'blue' in alien_colors:
    print("Faaaail")

# 5-4 alien colors #2
print("\nthis one is an if chain")

alien_colors2 = ['green']

if 'green' in alien_colors2:
    print("You just earned 5 points!")
if 'green' in alien_colors2:
    print("You just earned 10 points")

print("\nthis one is an if block")

alien_colors3 = ['green']

if 'green' in alien_colors3:
    print("you just earned 5 points")
elif 'green' in alien_colors3:
    print("you just earned 10 points")

# 5-5 alien colors #3
print("\nalien colors green")
alien_colors_green = ['green']

if 'green' in alien_colors_green:
    print("You've earned 5 points")
elif 'yellow' in alien_colors_green:
    print("You've earned 10 points")
elif 'red' in alien_colors_green:
    print("You've earned 15 points")

print("\nalien colors yellow")
alien_colors_yellow = ['yellow']

if 'green' in alien_colors_yellow:
    print("You've earned 5 points")
elif 'yellow' in alien_colors_yellow:
    print("You've earned 10 points")
elif 'red' in alien_colors_yellow:
    print("You've earned 16 points")

print("\nalien colors red")

alien_colors_red = ['notred']

if 'green' in alien_colors_red:
    print("You've earned 5 points")
elif 'yellow' in alien_colors_red:
    print("You've earned 10 points")
elif 'red' in alien_colors_red:
    print("You've earned 15 points")
else: print("i don't know")

# 5-6 Stages of Life

print("\nLIFE STAGES")
age = 38

if age < 2:
    print("You are a baby")
elif age < 4:
    print("You are a toddler")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult")
else:
    print("You are an elder")

# 5-7 Fruit
print("\nFRUIT CHECKLIST, I GUESS")
favorite_fruits = ['strawberries', 'bananas', 'raspberries']

if 'strawberries' in favorite_fruits:
    print("Wow you must really like strawberries")
if 'bananas' in favorite_fruits:
    print("Wow you must really like bananas")
if 'raspberries' in favorite_fruits:
    print("Wow you must really like raspberries")
if 'blackberries' in favorite_fruits:
    print("Wow you must really like blackberries")
if 'papaya' in favorite_fruits:
    print("Wow you must really like papayas")