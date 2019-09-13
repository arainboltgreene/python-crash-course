# 4-10 Slices

oddnum = list(range(1, 20, 2))
for num in oddnum:
    print(num)

print("the first three items in the list are:")
for num in oddnum[:3]:
    print(num)
print("three items from the middle of the list are:")
for num in oddnum[4:7]:
    print(num)
print("the last three items on my list are:")
for num in oddnum[-3:]:
    print(num)

# 4-11 My Pizzas, Your Pizzas

my_pizzas = ['angry vegan', 'baked potato', 'hot garlic']
friend_pizza = my_pizzas[:]
my_pizzas.append('new pizza')
friend_pizza.append('different pizza')

print("My favorite pizzas are:")
print(my_pizzas)
print("My friend's favorite pizzas are:")
print(friend_pizza)
