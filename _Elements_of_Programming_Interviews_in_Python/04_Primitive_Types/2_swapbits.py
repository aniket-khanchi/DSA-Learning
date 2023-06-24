a = 73   # 01001001
i = 1
j = 6

# 37 >> 4 = 2 (000010)
# 37 >> 1 = 18 (010011)

def swap_bits(x, i, j):
    if (x >> i)&1 != (x >> j)&1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
        return x
    

print(swap_bits(73,1,6))