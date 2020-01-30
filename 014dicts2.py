# 6-4 Glossary 2

print("\nSome words that of which I learneded:")
glossary = {
    'string': "kind of like a container.",
    'tuple': "like a list. but not.",
    'conditional': "like god's love",
    'loop': "weeeeeeee who cares this is boring",
    'print': "like showing the thing",
    'new1': "new1",
    'new2': "new2",
    'new3': "new3",
    'new4': "new4",
    'new5': "new5"
}

for key, value in glossary.items():
    print("\nKey: " + key)
    print("Value: " + value)

# 6-5 Rivers

rivers = {
    'amazon': "brazil",
    'nile': "egypt",
    'yangtze': "china"
}

print("\nloop to print a sentence about each river:")
for river, country in rivers.items():
    print(river.title() + " is in " +
        country.title() + ".")

print("\nloop to print name of each river:")
for river in rivers.keys():
    print(river.title())

print("\nloop to print each country:")
for river in rivers.values():
    print(river.title())

# 6-6 Polling - ???????

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

pollers = ['jen', 'edward', 'bella']
for name in favorite_languages.keys():
    print(name.title())

    if name in pollers:
        print("\n Thanks " + name.title() +
              ", I see you took the poll")
    else:
        print("You didn't take the poll")
