"""Demonstrations of dictoinary capabilities."""


# declare the type of a dictionary

# initialize to an empty diciontary 
schools = dict()

# set a key value pairing in the dictionary 
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# print a dictionary literal representation
print(schools) 

# Access a value by its key
print(f"UNC has {schools['UNC']} students.")

# Remove a key value pair from a dictionary using its key
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

print(schools)

# update / Reassign a key value pair 
schools["UNC"] = 20000
schools["NCSU"] += 200

# empty dictionary literal 
schools = {} # same as dict()
print(schools)

# You can also intitialize key value pairs 
schools = {
    "UNC": 19400,
     "Duke": 6717,
      "NSCU": 26150}
print(schools)