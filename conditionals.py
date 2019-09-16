# 5-1 Conditional tests

print("These things I predict to be true")

# true
doll = 'owned'
print("is doll == 'owned'? i predict true")
print(doll == 'owned')

# true
drinker = 21
print("can drinker legally drink? i predict true")
print(drinker == 21)

# true
cat = ['happy', 'healthy']
print("is cat happy OR healthy? i predict true")
print('happy' in cat) or ('healthy' in cat)

# true
# true

print("\nThese things I predict to be false:")

# false
keys = 'notowned'
print("is keys == 'owned'? I predict false")
print(keys == 'owned')

# false
cat = ['happy', 'healthy']
print("is cat happy AND healthy? i predict false")
print(cat == 'happy') and (cat == 'unhealthy')

# false
# false
# false
