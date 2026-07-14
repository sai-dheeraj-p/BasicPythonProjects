a1="-"*100
dict1={1:'hello',2:'drj'}
print('dict :',dict1)
print(a1)

dict1 = {}
dict2 = {"name": "drj", "age": 20, "city": "Hyd"}  #{}
dict3 = dict(name="dheeraj", age=20, city="hyderabad")  #dict()
print("Empty Dictionary:", dict1)
print("Dictionary 1 (created using {}):", dict2)
print("Dictionary 2 (created using dict()):", dict3)
print(a1)

dict3 = {
    "name": "drj",
    "age": 20,
    "gender": "male",
    "profession": "engineer"
}
#print("given dict :",dict3)
print("My Details")
print("Name:", dict3["name"])
print("Age:", dict3["age"])
print("Gender:", dict3.get("gender"))
print("Profession:", dict3.get("profession"))
print(a1)

dict1 = {
    "name": "abc",
    "age": 99,
    "gender": "male",
    "profession": "idle"
}
print("Given Dictionary:", dict1)
dict1["country"] = "zimbabwe" #adding element in dict
print("Updated Dictionary:", dict1)
print(a1)

dict_x = {
    "name": "mno",
    "age": 33,
    "gender": "male",
    "profession": "painter",
    "country": "netherlands"
}
print("Given Dictionary:", dict_x)
del dict_x['age']  #del
print("Updated Dictionary (Removed 'age'):", dict_x)
popped_value = dict_x.pop('gender')  #pop()
print("Updated Dictionary (Removed 'gender'):", dict_x)
print("Popped Value:", popped_value)
popped_item = dict_x.popitem()  #popitem()
print("Updated Dictionary (Removed last item):", dict_x)
print("Popped Item:", popped_item)
dict_x.clear()  #clear()
print("Update Dictionary (Removed all items):", dict_x)
print(a1)

dict3 = {
    "name": "drj",
    "age": 20,
    "gender": "male",
    "profession": "engineer"
}
print("given dict :",dict3)
dict3['name']="dheeraj"
dict3['age']=30
print("updated dict :",dict3)
print(a1)

dict3 = {
    "name": "drj",
    "age": 20,
    "gender": "male",
    "profession": "engineer"
}
print("Items in Dictionary:")
for key in dict3:
  value = dict3[key]
  print(key, "->", value)
print(a1)

dict3 = {
    "a": "a1",
    "b": 30,
    "c": "bbb",
    "d": "efcdwws"
}
print("given data:",dict3)
print("size of the dict:",len(dict3))
print(a1)

dicty = {
    'fruit': 'apple',
    'vegetable': 'onion',
    'dry-fruit': 'resins'
}
print("dicty:",dicty)
print("Is 'fruit' a member of 'dicty'?:", 'fruit' in dicty)
print("Is 'beverage' a member of 'dicty'?:", 'beverage' in dicty)
print("Is 'beverage' NOT a member of 'dicty'?:", 'beverage' not in dicty)
print(a1)
