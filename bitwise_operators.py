print("this is a bitwise operator example")
a = 10  # 1010
b = 12  # 1100

print("a & b (AND):", a & b)
print("a | b (OR):", a | b)
print("a ^ b (XOR):", a ^ b)
print("~a (NOT):", ~a)
print("a << 1 (Left Shift):", a << 1)
print("a >> 1 (Right Shift):", a >> 1)
#=======================EXPLANATION========================
# a=0b1010
# b=0b1100
# c=a&b
# print(bin(c))
# output = 0b1000
#because    1010
#                1100
#                ------
#                1000
# 0b1000 = 8 in decimal

#a|b = 0b1010 | 0b1100
# output = 0b1110
# because    1010
#                1100
#                ------
#                1110
# 0b1110 = 14 in decimal
# a^b = 0b1010 ^ 0b1100
# output = 0b0110
# because    1010
#                1100
#                ------
#                0110
# 0b0110 = 6 in decimal
# ~a = 0b1010
# output = 0b0101
# because    1010
#                ------
#                0101
# 0b0101 = 5 in decimal
#5 is a positive number so there's 0 in the leftmost bit
#so the output would be 10101 but the leftmost bit is 1 so it would be negative
#we don't represent negative numbers directly in system
#we use 2's complement to represent negative numbers
#we take the 1's complement of the number and add 1 to it
#so the output would be 10101 + 1 = 10110
#so the output would be 10110
# 0b10110 = -11 in decimal
# a<<1 = 0b1010 << 1
# output = 0b10100
# because    1010
#                ------
#                10100
# 0b10100 = 20 in decimal
# a>>1 = 0b1010 >> 1
# output = 0b0101
# because    1010
#                ------
#                0101
# 0b0101 = 5 in decimal
