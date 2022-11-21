# c=""



# while c !="stop":
#     c=input('What is your grade?  ')
    
    
# lst=int(input("Enter your grades"))

# x=[]

# sum=0

# for grade in x:
#     sum=sum+grade

# print(sum/len(x))



# # input size of the list
# n = int(input("Enter the number of grades : "))
# # store integers in a list using map, split and strip functions
# x = list(map(int, input(
#     "Enter your grades(Space-Separated): ").strip().split()))[:n]
# print('The list is:', x)   # printing the list

 
 
# lst=[x]

# sum=0

# for grade in lst:
#     sum=sum+grade

# print(sum/len(x))




input_string = input('Enter grades separated by space ')
print("\n")
# Take input numbers into list
numbers = input_string.split()

# convert each item to int type
for i in range(len(numbers)):
    # convert each item to int type
    numbers[i] = int(numbers[i])

# Calculating the sum and average
print("Average = ", sum(numbers) / len(numbers))