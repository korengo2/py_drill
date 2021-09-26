# question 1:
nums = [4,7,1,9,4,5]
# print the list
print(nums)
# function:
i=0
while i<len(nums):
    key=i
    j=i+1
    while j<len(nums):
        if nums[key]>nums[j]:
            key=j
        j+=1
    nums[i],nums[key]=nums[key],nums[i]
    i+=1
# print the sorted list
print(nums)

#  question 2:
# function:
def findAvg(name,date_of_birth,class_num,math,english,physics):
  print("Name: ",name)
  print("Date of birth: ",date_of_birth)
  print("class number: ",class_num)
  print("All grades: \n","Math: ",math,"\n", "English: ",english,"\n" ',Physics: ',physics)
  avg = (math + english + physics)/3
  print("Your avarage is:",avg)

name = input("Name: ")
date_of_birth = input("Date of birth: ")
class_num = input("Class number: ")
math =  int(input("Math grade: "))
english =  int(input("English grade: "))
physics =  int(input("Phisics grade: "))

findAvg(name,date_of_birth,class_num,math,english,physics)

# question 3:
    
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
	
if num1<num2:
    if num1<num3:
        print("The lowest number is: ", num1)
    else:
        print("The lowest number is: ", num3)
elif num2<num1:
    if num2<num3:
        print("The lowest number is: ", num2)
    else:
        print("The lowest number is: ", num3)
        
# question 4:
    
name = input("Name: ")
all_names = []

while name!="=":
    all_names.append(name)
    name = input("Name: ")

print(all_names)