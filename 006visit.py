# 3-8 seeing the world

places = ['tokyo', 'amsterdam', 'salem', 'england', 'boston']

print("here is the original list:")
print(places)

print("here it is sorted:")
print(sorted(places))

print("here is the original list again:")
print(places)

print("and here it is in reverse alpha order:")
print(sorted(places, reverse=True))

print("See how it's still in the original order tho")
print(places)

print("and here it is reversed")
places.reverse()
print(places)

print("and here it is reversed back to it's original order")
places.reverse()
print(places)

print("here it is printed with sort (not sorted!)")
places.sort()
print(places)

print("here it is, reverse alpha sort (not sorted!)")
places.sort(reverse=True)
print(places)
