#Create a dictionary
my = {"name": "Anil",
      "university": "MEF University",
      "department": "Industrial Engineering",
      "hobbies": "reading history books"}
my
my["name"]
my["hobbies"]

#Adding New Values
my['favorite color'] = 'red'
my

#Editing Values
my['favorite color'] = 'purple'
my

#Deleting Values
del(my['favorite color'])
my

#Get Keys
print(my.keys())

#Get Values
print(my.values())

#Get All Items
print(my.items())

#Length of Dictionary (!Attention, each match counts as one)
print(len(my))

#Create a dictionary with different data types
mixed_dict = {0: "zero",
             "one": 1,
             "Correct": True,
             "Primes": [2, 3, 5, 7],
             }
mixed_dict

#List cannot be used as keys
# dummy_dict = {["list", "as", "key"]: 5}

#nested dictionary
films = {"avatar": {"year": 2009, "director": "james cameron", "duration": 162},
         "titanic": {"year": 1997, "director": "james cameron", "duration": 195}}
films
films["avatar"]
films["titanic"]["duration"]
