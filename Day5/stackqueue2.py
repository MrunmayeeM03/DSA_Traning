# Insert Element in Array

# arr = []

# n = int(input("Enter size: "))

# # Input array elements
# for i in range(n):

#     ele = int(input("Enter number: "))
#     arr.append(ele)

# print("Original Array:", arr)

# # Input key element
# key = int(input("Enter element to insert: "))

# # Input location
# loc = int(input("Enter location (0-based index): "))

# # Insert element
# arr.insert(loc, key)

# print("Array after insertion")




#Rotaion problem :  Rotate an array to the right by given number of steps.
# arr = [1, 2, 3, 4, 5]
# k = 2

# n = len(arr)

# for i in range(k):
#     last = arr[n-1]
#     for j in range(n-1, 0, -1):
#         arr[j] = arr[j-1]

#     arr[0] = last

# print(arr)





## Intersection of two arrays

# arr1 = [1, 2, 2, 3]
# arr2 = [2, 2]

# intersection = []

# for i in arr1:
#     if i in arr2 and i not in intersection:
#         intersection.append(i)

# print(intersection)







# Rearrange Positive and Negative Numbers Alternately
# Rearrange Positive and Negative Numbers Alternately

# arr = [-1, 2, -3, 4, 5, -6]

# positive = []
# negative = []

# # Separate positive and negative numbers
# for i in arr:
#     if i >= 0:
#         positive.append(i)
#     else:
#         negative.append(i)

# result = []

# i = 0
# j = 0

# # Arrange alternately
# while i < len(negative) and j < len(positive):
#     result.append(negative[i])
#     result.append(positive[j])

#     i = i + 1
#     j = j + 1

# # Remaining negative numbers
# while i < len(negative):
#     result.append(negative[i])
#     i = i + 1

# # Remaining positive numbers
# while j < len(positive):
#     result.append(positive[j])
#     j = j + 1

# print("Output:", result)


    


# Reverse a String without inbuilt function

# str1 = "hello"

# rev = ""

# for i in str1:
#     rev = i + rev

# print("Reversed String:", rev)





#check for a valid palindrome string:
#Question: write a program to check if a given string is a valid. palindrome string after ignoring non-alphanuric char and consider case
#logic: use loops to compare charecter while ignoring
 #non alphnumeric chartristicts  


 
# Check Valid Palindrome String

# str1 = input("Enter string: ")

# clean = ""

# # Keep only alphanumeric characters
# for ch in str1:
#     if ch.isalnum():
#         clean = clean + ch.lower()

# # Reverse string using loop
# rev = ""

# for ch in clean:
#     rev = ch + rev

# # Check palindrome
# if clean == rev:
#     print("Valid Palindrome")
# else:
#     print("Not a Palindrome")






#check for Anagrams
# Check for Anagrams

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Convert to lowercase
str1 = str1.lower()
str2 = str2.lower()

# Remove spaces
s1 = ""
s2 = ""

for ch in str1:
    if ch != " ":
        s1 = s1 + ch

for ch in str2:
    if ch != " ":
        s2 = s2 + ch

# Sort characters
a = sorted(s1)
b = sorted(s2)

# Check anagram
if a == b:
    print("Anagrams")
else:
    print("Not Anagrams")






    



