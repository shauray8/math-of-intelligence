# FULL ADDER
""" How does a full adder wor?
It adds 3 inputs and produces first 2 inputs A and B and a carry bit C
"""
import argparse

def fulladder(a, b, carry) -> any:
    xor1 = a ^ b
    fsum = xor1 ^ carry
    and1 = a & b
    and2 = xor1 & carry
    cout = and1 | and2
    return fsum, cout

def main(A:int, B:int) -> int:
    first = bin(A).replace("0b","")
    second = bin(B).replace("0b","")

    x,y = first[::-1], second[::-1] 
    while len(x) < 8:
        x += '0'
        first = x[::-1]
    while len(y) < 8:
        y += '0'
        second = y[::-1]
    a = [i for i in first]
    b = [i for i in second]
    return a,b

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('A', metavar='N', type=int, nargs='+',
                        help='Enter an integer for addition')
    parser.add_argument('B', metavar='M', type=int, nargs='+',
                        help='Enter another interger for addition')

    args = parser.parse_args()
    a,b = main(args.A[0], args.B[0])
    
    carry = 0
    out = []
    for i in range(1,len(a)+1):
        #print("first",a[-i], "second",b[-i], "carry",carry)
        add, carry = fulladder(int(a[-i]),int(b[-i]),carry)
        #print("add",add, "carry",carry)
        out.append(str(add))

    out.append(str(carry))
    seperator = ""
    print("addding",args.A[0], "and", args.B[0])
    print(seperator.join(out[::-1]))
