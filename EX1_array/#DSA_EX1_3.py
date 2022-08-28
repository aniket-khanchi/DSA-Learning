#DSA_EX1_3
# Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function.

max_num = input("enter the max no.:" )
sol = []
for i in range(int(max_num)+1):
    if i%2 == 0:
        continue
    else:
        sol.append(i)

print(sol)        

#Given Solution
max = int(input("Enter max number: "))

odd_numbers = []

for i in range(max):
    if i%2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ",odd_numbers)