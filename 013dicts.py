# 6-1 Person


person = {'first_name': 'm.', 'last_name': 'e.', 'age': '49', 'city': 's. b.'}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6-2 Favorite Numbers


print("\nPeople's favorite numbers:")

favorite_numbers = {
    'm.': 23,
    'angela': 9,
    'kurtis': 1,
    'beverly': 4,
    'adrian': 9001,
}

print("M.'s favorite number is " + str(favorite_numbers['m.']) + ".")
print("angela's favorite number is " + str(favorite_numbers['angela']) + ".")
print("kurtis' favorite number is " + str(favorite_numbers['kurtis']) + ".")
print("beverly's favorite number is " + str(favorite_numbers['beverly']) + ".")
print("adrian's favorite number is " + str(favorite_numbers['beverly']) + ".")

# 6-3 Glossary

print("\nSome words that of which I learneded:")
glossary = {
    'string': "kind of like a container.",
    'tuple': "like a list. but not.",
    'conditional': "like god's love",
    'loop': "weeeeeeee who cares this is boring",
    'print': "like showing the thing"
}
# need to figure out how to indent after the \n
print("String: \n" + glossary['string'])
print("tuple: \n" + glossary['tuple'])
print("conditional: \n" + glossary['conditional'])
print("loop: \n" + glossary['loop'])
print("print: \n" + glossary['print'])