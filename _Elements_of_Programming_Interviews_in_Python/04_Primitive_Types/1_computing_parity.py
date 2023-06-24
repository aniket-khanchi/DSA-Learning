a = 12  # binary: 1100
b = 5   # binary: 0101

bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b
bitwise_not_a = ~a
left_shift_a = a << 2
right_shift_b = a >> 1

print("Bitwise AND:", bitwise_and)        # Output: 4
print("Bitwise OR:", bitwise_or)          # Output: 13
print("Bitwise XOR:", bitwise_xor)        # Output: 9 -- XOR gate is a digital logic gate that gives a true output when the number of true inputs is odd.
print("Bitwise NOT (a):", bitwise_not_a)  # Output: -13 (dependent on the number of bits)
print("Left Shift (a):", left_shift_a)    # Output: 48 (decimal) or 110000 (binary)
print("Right Shift (b):", right_shift_b)  # Output: 2 (decimal) or 0010 (binary)


#Count Bits

def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# x = count_bits(10)
# print(x)


#check parity if no of 1 is odds then 1 else 0
def parity(x):             #x and x-1 equals x with its lowest set it erased.
    result = 0
    while x:
        result ^= 1
        x &= x-1
    return result

q = parity(11)  # 1011
print(q)

