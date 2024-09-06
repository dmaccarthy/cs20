"""
CSE 2120: Data Structures
Dictionaries & Sets
Example 9

"""

myFriend = {
    "name": "Jane Doe",
    "email": "jdoe@eips.ca",
    "birthday": "2005-11-02",
    "phone": "780-555-5555"
}

print("Jane Doe" in myFriend)
print("name" in myFriend)
print("Jane Doe" in myFriend.values())
print("name" in myFriend.values())
