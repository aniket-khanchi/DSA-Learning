'''
Given: An array of non-negative digits that represent a decimal integer.

Problem: Add one to the integer. Assume the solution still works even if implemented 

in a language with finite-precision arithmetic.
'''
A1 = [1, 4, 9]
A2 = [9, 9, 9]

# s = ''.join(map(str, A))
# print(int(s) + 1)


def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


print(plus_one(A1))
print(plus_one(A2))

def plus_one_me(A):
    carry = 1
    itr = -1
    for i in range(len(A)):
        if A[itr] + carry < 10:
            A[itr] += carry
            return A
        else:
            if itr == -len(A):
                A[itr] += carry
                carry =  int(str(A[itr])[0])
                A[itr] = int(str(A[itr])[-1])
                A.insert(0,carry)
                return A
            A[itr] += carry
            carry =  int(str(A[itr])[0])
            A[itr] = int(str(A[itr])[-1])
            itr -= 1

print(plus_one_me([9,9,0]))

