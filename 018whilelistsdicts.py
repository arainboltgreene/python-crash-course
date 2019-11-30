# 7-8 Deli

sanny_orders = ['pastrami', 'pb&j', 'chickpea salad', 'pastrami', 'tlt', 'pastrami']
finished_sannies = []

print("\nWe've run out of pastrami. Oh darn.")

while 'pastrami' in sanny_orders:
    sanny_orders.remove('pastrami')

while sanny_orders:
    current_sanny = sanny_orders.pop()

    print("Making sandwich: " + current_sanny)
    finished_sannies.append(current_sanny)

print("\nThe following sannies have been made:")
for finished_sanny in finished_sannies:
    print(finished_sanny)

# 7-9 no pastrami

