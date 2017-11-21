# import math

# # 0xB105F00D	2969956365	1011 0001 0000 0101 1111 0000 0000 1101

# # 0x7BFB2000	2080055296	0111 1011 1111 1011 0010 0000 0000 0000

# x = 0xB105F00D
# y = 0x7BFB2000

# print(str(hex(x)) + "       " + str(hex(y)) + "\n")

# print(str(hex(x * y)) + " = NOT IT")
# print(str(math.sqrt(x + y)) + " = NOT IT")
# print(str(hex(x - y)) + " = NOT IT")  

# print(math.sqrt(x))

n = [1, 2, 3, 4, 6, 7, 8]

p = (len(n) *(len(n) + 2)/2)

a = sum(n)

print(p)

print(a)

print(p - a)