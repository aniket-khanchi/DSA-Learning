# #DSA_EX1
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190

# Create a list to store these monthly expenses and using that find out,
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. 
# Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

#ANS1
exp = [2200,2350,2600,2130,2190]
print(str(exp[1]-exp[0]) + " dollars ")

#ANS2
print(str(sum(exp[0:3])) + " dollars")

#ANS3
for i in exp:
    count = 0
    if i == 2000:
        print("yes")
        count +=1
    else:
        continue
# print("there are total "+ str(count)+" dollars")    
if count ==0:
    print("there is no tarnsaction of $2000.")
else:
    print("there is total" + "count" + "transactions of $2000.")

#ANS4
exp.append(1980)
print(exp)

#ANS5
exp[3] = exp[3] -200
print(exp)

#Given Solution

# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

exp = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("In feb this much extra was spent compared to jan:",exp[1]-exp[0]) # 150

# 2. Find out your total expense in first quarter (first three months) of the year
print("Expense for first quarter:",exp[0]+exp[1]+exp[2]) # 7150

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", 2000 in exp) # False

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print("Expenses at the end of June:",exp) # [2200, 2350, 2600, 2130, 2190, 1980]

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3] = exp[3] - 200
print("Expenses after 200$ return in April:",exp) # [2200, 2350, 2600, 1930, 2190, 1980]












