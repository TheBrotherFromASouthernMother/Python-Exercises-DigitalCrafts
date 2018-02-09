


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

def fib(n, n2, limit, arr):
    if n + n2 >= limit:
        return n + n2
    else:
        return 

def printFib():
    evenValsFib = [1, 2]




#2. Algo2
def findMultiples(length):
  sum = 0
  for i in range(length):
    if i % 5 == 0:
      sum += i
    elif i % 3 == 0:
      sum += i
  # print(sum)
  return sum

findMultiples(1000) # 233168

#3. Algo3

def fibonacci(limit):
  sum = 0
  nPrev = 0
  n = 1
  while n < limit:
		nPrev = n
    n = nPrev + n
    if n % 2 == 0:
      sum += n
  return sum
  
  
  
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

#4 Algo 4
def findLargestPrimeFactor(number):
  largestPrime = 2
  for i in range(2, number+1):
    if number % i == 0 and :
      largestPrime = i
      print(largestPrime)
  
  return largestPrime

findLargestPrimeFactor(13195)   
