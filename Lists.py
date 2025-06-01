# List Method
# Positive Indexing
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])

# Negative Indexing
colorl = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colorl[-1])
print(colorl[-3])
print(colorl[-5])

# To check the items is present in the list we do following work
if "Red" in colors:
    print("Yes, Red is present in the list")
else:
    print("No, Red is not present in the list")

# Range of Indexes
print(colors[1:4])    
print(colors[-7:-2])
print(colorl[1:8:3])

# List Comprehsion
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

# List Methods
# Sort
colors.sort()
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

# Reverse
colors.reverse()
print(colors)

# index
print(colors.index("green"))

# count
print(colors.count("green"))

# copy
newlist = colors.copy()

# append
colors.append("green")