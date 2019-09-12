# 3-4

guests = ['doth the doth', 'jenna marbles', 'maya angelou']

message0 = "Hello, " + guests[0].title() + " you are invited to dinner."
print(message0)
message1 = "Hello, " + guests[1].title() + " you are invited to dinner."
print(message1)
message2 = "Hello, " + guests[2].title() + " you are invited to dinner."
print(message2)

# 3-5 changing guest list

print("Jenna Marbles can't make it.")

guests.remove('jenna marbles')
print(guests)

guests.append('sappho')
print(guests)

message0 = "Hello, " + guests[0].title() + " you are invited to dinner."
print(message0)
message1 = "Hello, " + guests[1].title() + " you are invited to dinner."
print(message1)
message2 = "Hello, " + guests[2].title() + " you are invited to dinner."
print(message2)

# 3-6 more guests

print("Oh goodie. I found a bigger dinner table. 3 more people are invited.")

guests.insert(0, 'stephen king')
guests.insert(2, 'idris alba')
guests.append('michelle obama')

message0 = "Hello, " + guests[0].title() + " you are invited to dinner."
print(message0)
message1 = "Hello, " + guests[1].title() + " you are invited to dinner."
print(message1)
message2 = "Hello, " + guests[2].title() + " you are invited to dinner."
print(message2)
message3 = "Hello, " + guests[3].title() + " you are invited to dinner."
print(message3)
message4 = "Hello, " + guests[4].title() + " you are invited to dinner."
print(message4)

# 3-7

print("Ok I guess now I only have room for 2 people.")
print(guests)
sorry = guests.pop(0)
print('Sorry ' + sorry.title() + '.')
sorry = guests.pop(1)
print('Sorry ' + sorry.title() + '.')
sorry = guests.pop(2)
print('Sorry ' + sorry.title() + '.')
print(guests)
