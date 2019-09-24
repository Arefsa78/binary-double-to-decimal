# 0 10000001010 1001001100000000000000000000000000000000000000000000
# 1627.7421875
binary = input("bin: ").split(' ')
print(len(binary[1]))

s = (-1) ** int(binary[0])
c = sum([(2 ** (11 - i - 1)) * int(b) for i, b in enumerate(binary[1])])
f = sum([(0.5 ** (i + 1)) * int(b) for i, b in enumerate(binary[2])])

print(s, c, f)

n = s * (2 ** (c - 1023)) * (1 + f)
print(n)
