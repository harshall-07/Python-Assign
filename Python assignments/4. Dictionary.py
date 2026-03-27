d1 = {}
print(type(d1))

d2 = { "Raaj": "mango" , "Sanu": "banana" , "Rahul": "guava" }
print(d2)
print(d2["Raaj"])                                                      #we can use either line 6 or 7 ,output will be same
print(d2.get("Raaj"))

d2["Harsh"] = "kiwi"                                                    #addition of new key pair in dictionary
print(d2)

del d2["Harsh"]                                                         #removing/deleting of key pair
print(d2)

print(d2.copy())                                                        #create shallow copy of dictionary
print(d2)


d2.update({"Raaj": "papaya"})                                           #updating the dictionary with new word
print(d2)

print(d2.keys())                                                       #display all keys in the dictionary

print(d2.values())                                                     #display all values from the dictionary

print(d2.items())                                                      #display all key-value pairs



