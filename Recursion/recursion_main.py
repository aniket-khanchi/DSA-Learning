# this file is to simplify recursion,


def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


#fibonacci Sequence 
# Recursive function
def recursive_fibonacci(n):
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 10
 
# check if the number of terms is valid
if n_terms <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("Fibonacci series:")
for i in range(n_terms):
    print(recursive_fibonacci(i))  

# The factorial of 6 is denoted as 6! = 1*2*3*4*5*6 = 720. 

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))
 
# check if the input is valid or not
# if num < 0:
#   print("Invalid input ! Please enter a positive number.")
# elif num == 0:
#   print("Factorial of number 0 is 1")
# else:
#   print("Factorial of number", num, "=", recursive_factorial(num))






