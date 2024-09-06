"""
CSE 2120: Data Structures
Dictionaries & Sets
Example 7

"""

myFriend = {
    "name": "Jane Doe",
    "email": "jdoe@eips.ca",
    "birthday": "2005-11-02",
    "phone": "780-555-5555"
}
myFriend["hobbies"] = "Soccer", "Running", "Computer Programming"
del myFriend["email"]
print(myFriend)
