


# def printFizzBuzz(length):
#     for i in range(length + 1):
#         if i % 15 == 0:
#             print(i, "FizzBuzz")
#         elif i % 5 == 0:
#             print(i, "Buzz")
#         elif i % 3 == 0:
#             print(i, "Fizz")

      

# printFizzBuzz(100)


# def fibonacci(n, limit, sum):
#   nPrev = 
#   n =
#   sum =  
#   sum += n
#   print(n)
#   if n >= limit:
#     return sum
#   else:
#     return fibonacci(n+n, limit, sum)



# def summingFunc():
#   sum = fibonacci(1, 10, 0)
#   print(sum)
#   return sum

# summingFunc()

# def F(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return F(n-1)+F(n-2)

# def fibValues():
#     a = F(2)
#     if a > 100:
#         print(a)
#         return a

# fibValues()
# print("Gha")

sum = 0
for i in range(1, 10):
    for j in range(i, 10, i):
        if j > 0:
            print(j)