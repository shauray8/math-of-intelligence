#SR latch or multiplexer

Q, Q_dash = 0, 0
def sr(s, r, Q, Q_dash):
    first_or = r | Q_dash
    first_or = ~first_or
    print(first_or)
    second_or = s | Q
    second_or = ~second_or
    Q = first_or
    Q_dash = second_or

    print(Q, Q_dash)


sr(1,0, Q, Q_dash)

