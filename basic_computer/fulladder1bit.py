# FULL ADDER

first = bin(167).replace("0b","")
second = bin(33).replace("0b","")

x = first[::-1] 
y = second[::-1] 
while len(x) < 8:
    x += '0'
    first = x[::-1]
while len(y) < 8:
    y += '0'
    second = y[::-1]

def fulladder(a, b, carry):
    xor1 = a ^ b
    fsum = xor1 ^ carry
    and1 = a & b
    and2 = xor1 & carry
    cout = and1 | and2
    return fsum, cout

a = [i for i in first]
#print(a)
b = [i for i in second]
#print(b)

carry = 0
out = []
for i in range(1,len(a)+1):
    #print("first",a[-i], "second",b[-i], "carry",carry)
    add, carry = fulladder(int(a[-i]),int(b[-i]),carry)
    #print("add",add, "carry",carry)
    out.append(str(add))

out.append(str(carry))
seperator = ""
print("addding",first, "and", second)
print(seperator.join(out[::-1]))
