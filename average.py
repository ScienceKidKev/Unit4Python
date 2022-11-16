# c=""



# while c !="stop":
#     c=input('What is your grade?  ')
    
    

# x=[44, 67, 85,0]

# sum=0

# for grade in x:
#     sum=sum+grade

# print(sum/len(x))



# input size of the list
n = int(input("Enter the number of grades : "))
# store integers in a list using map, split and strip functions
lst = list(map(int, input(
    "Enter your grades(Space-Separated): ").strip().split()))[:n]
print('The list is:', lst)   # printing the list

 
 
lst=[n]

sum=0

for grade in lst:
    sum=sum+grade

print(sum/len(lst))

