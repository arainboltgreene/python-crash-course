def describe_pet(pet_name, animal_type ='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('willie')

# 8 - 3/4 t shirt

def make_shirt(message, size = "large"):
    print("\n This shirt is a " + size + " and it says " + message + ".")

make_shirt(message = "I love Python")
make_shirt(message = "a message", size = "medium")

# 8-5 Cities

def describe_city(city, country = "Iceland"):
    print("\nthe city " + city + " is in " + country + ".")

describe_city("Reykjavik")
describe_city("Kopavogur")
describe_city(city = "Salem", country = "USA")