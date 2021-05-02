# soon building a full adder for 8 bits
a = 0
b = 1
carry = 1
for i in range(1):
    xor1 = a ^ b
    fsum = xor1 ^ carry
    and1 = a & b
    and2 = xor1 & carry
    cout = and1 | and2
    print("sum:",fsum,"carry:", cout)
