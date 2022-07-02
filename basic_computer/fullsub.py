# full subtractor with logic gates

a = 1
b = 0

def sub(a, b, c):
    first_xor = a ^ b
    a = ~a
    first_and = a & b
    diff = first_xor ^ c
    first_xor = ~first_xor
    second_and = c & first_xor
    b_out = first_and & second_and

    print(b_out)


sub(a,b,0)
