import json

# Place the data in dictionaries...

contact1 = {"surname": "MacCarthy", "email": "dmaccarthy@eips.ca",
    "address": "Room 140, 20 Festival Way", "city": "Sherwood Park, AB",
    "phone": "780-467-8816", "details": "Comp Sci Teacher"}

contact2 = {"surname": "Doe", "givenName": "Jane",
    "email": "janedoe@gmail.com"}

# Dump (save) the dictionary as a JSON file...

allContacts = {"contacts": [contact1, contact2]}
with open("contacts.json", "w", encoding="UTF-8") as f:
    json.dump(allContacts , f, ensure_ascii=False)

# Reload the JSON file...

with open("contacts.json", encoding="UTF-8") as f:
    print(json.load(f)["contacts"])