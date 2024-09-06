"""
CSE 2120: Data Structures
Dictionaries & Sets
Example 8

"""

myFriend = {
    "name": "Jane Doe",
    "email": "jdoe@eips.ca",
    "birthday": "2005-11-02",
    "phone": "780-555-5555"
}

print("Keys...")
for x in myFriend:
    print(x)

print("\nValues...")
for x in myFriend.values():
    print(x)

print("\n(Key, Value) Tuples...")
for x in myFriend.items():
    print(x)
