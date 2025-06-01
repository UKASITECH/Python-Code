info = {"Carla", 19, False, 5.9, 19}
print(info)

# Accessing set items:
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)

# Dictionary
# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info) 
# print(info.keys())
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}")     