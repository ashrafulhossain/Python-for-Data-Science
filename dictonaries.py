# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:

dic = {
    'Harry': 'Huming Being',
    'Spon': 'Object'
}
print(dic)
print(type(dic))

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict)

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

#access

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict['brand'])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


data_science = {
    'Ml' : 'sk_learn',
    'Dl' : 'Tenserflow',
    'DA' : 'Power Bi',
    'NLP' : 'NLTk'
}
print(data_science)

x = data_science.keys()
print(x)
data_science['Network'] = 'Lan'
print(data_science)
x = data_science.items()
print(x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")