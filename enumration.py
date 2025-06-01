marks = [5,8,9,450,55,1,15,151,51,58]
index = 0
for mark in marks:
    print(mark)
    if (index==3):
        print("Umang , Awesome!!!")
    index += 1

print("\n\n")

# enumration using enumarate instead of index += 1

for index,mark in enumerate(marks):
    print(mark)
    if (index==3):
        print("Umang , Awesome!!!")   