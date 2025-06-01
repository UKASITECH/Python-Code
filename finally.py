a = input("Enter a number :")

try:
    for i in range(1,11):
     print(f" {int(a)} X {i} is = {int(a)*i}")
except Exception as e:
    print("Soory Bhai tum ek number enter karo naki kuch orr")    

finally:
   print("I am always excuted")   