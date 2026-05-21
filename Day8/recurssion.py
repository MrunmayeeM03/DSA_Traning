#recurrsion function():
# a function which is called itself repetedly till condition is satsified is called reursion function
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# if __name__ =='__main__':
#     n= 5
#     res= factorial(n)
#     print(res)  
#     n=5
#     factorial(5)
#     5*factorial(4)
#     4*factorial(3)
#     3*factorial(2)
#     2*factorial(1)
#     1



# def multiply(x, y):
#     if y == 1:
#         return x
#     elif x == 1:
#         return y
#     elif x == 0 or y == 0:
#         return 0
#     else:
#         return x + multiply(x, y - 1)

# def main():
#     print("Multiplication =", multiply(5, 4))



#---------find power----------#

# def power(x, y):
#     if y==0:
#         return 1
#     else:
#         return x * power(x, y - 1)

# def main():
#     print("Power =", power(2, 5))

# if __name__ == "__main__":
#     main()


#--------------------find sum of N using Recurssion------------------
#n=10 -> 55

# def find_sum(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return n + find_sum(n - 1)

# def main():
#     print("Sum =", find_sum(10))

# if __name__ == "__main__":
#     main()


#------------------------------------fibonacci series------------------------------------------------------------------------------

# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)

# def main():
#     n = 10

#     for x in range(n):
#         print("fibo =", fibo(x))

# if __name__ == "__main__":
#     main()




