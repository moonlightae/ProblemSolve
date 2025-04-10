def modin(a, m):
    if gcd(a, m) != 1:
        return a

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)