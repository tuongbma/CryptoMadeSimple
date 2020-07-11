import math

def check_interval(x, q):
    if (0 <= x <= round(q/3)): #s1
        return 1
    if (round(q/3) + 1 <= x <=  round(2*q/3)): #s2
        return 2
    if (round(2*q/3) + 1 <= x <= q-1): #s3
        return 3

def calculate_by_interval(interval, x, a, b, q,p, g, h):
    if (interval == 1): #s1
        new_x = (h * x) % q
        new_a = a % p
        new_b = (b + 1) % p

    if (interval == 2): #s2
        new_x = (x * x) % q
        new_a = (2 * a) % p
        new_b = (2 * b) % p

    if (interval == 3): #s3
        new_x = (g*x) % q
        new_a = (a + 1) % p
        new_b = b % p

    return new_x, new_a, new_b

def find_x_integer(ai, a2i, bi, b2i, p):
    for j in range (1, (bi-b2i)):
        x = ((a2i-ai) + p*j)/(bi-b2i)
        if (x == int(x)): # x is integer
            return int(x)

def polars_rho(q, p, g, h):
    x, a, b = [1]*q, [0]*q, [0]*q

    for i in range (0, q): 
        j = 2*i
        if (j >= q): # list out of index
            break
        # print(b[i], "-", b[j])

        if (x[i] == x[j]):
            # print(x[i], "-", x[j])
            if (b[i] != b[j]): # if b[m] != b[2m]
                solution = find_x_integer(a[i], a[j], b[i], b[j], p)
                return solution

        if (check_interval(x[i],q) == 1): #s1
            x[i+1], a[i+1], b[i+1] = calculate_by_interval(1,x[i],a[i],b[i],q,p,g,h)

        if ((check_interval(x[i],q) == 2)): #s2
            x[i+1], a[i+1], b[i+1] = calculate_by_interval(2,x[i],a[i],b[i],q,p,g,h)

        if ((check_interval(x[i],q) == 3)): #s3
            x[i+1], a[i+1], b[i+1] = calculate_by_interval(3,x[i],a[i],b[i],q,p,g,h)

        #calculate x[2(i+1)] = x[2i + 2]
        if (check_interval(x[j],q) == 1): #s1
            x[j+1], a[j+1], b[j+1] = calculate_by_interval(1,x[j],a[j],b[j],q,p,g,h)
            if (check_interval(x[j+1],q) == 1): #s1
                x[j+2], a[j+2], b[j+2] = calculate_by_interval(1,x[j+1],a[j+1],b[j+1],q,p,g,h)
            if (check_interval(x[j+1],q) == 2): #s2
                x[j+2], a[j+2], b[j+2] = calculate_by_interval(2,x[j+1],a[j+1],b[j+1],q,p,g,h)
            if (check_interval(x[j+1],q) == 3): #s3
                x[j+2], a[j+2], b[j+2] = calculate_by_interval(3,x[j+1],a[j+1],b[j+1],q,p,g,h)

        if ((check_interval(x[j],q) == 2)): #s2
            x[j+1], a[j+1], b[j+1] = calculate_by_interval(2,x[j],a[j],b[j],q,p,g,h)
            if (check_interval(x[j+1],q) == 1): #s1
                x[j+2], a[j+2], b[j+2] = calculate_by_interval(1,x[j+1],a[j+1],b[j+1],q,p,g,h)
            if (check_interval(x[j+1],q) == 2): #s2
                x[j+2], a[j+2], b[j+2] = calculate_by_interval(2,x[j+1],a[j+1],b[j+1],q,p,g,h)
            if (check_interval(x[j+1],q) == 3): #s3
                x[j+2], a[j+2], b[j+2] = calculate_by_interval(3,x[j+1],a[j+1],b[j+1],q,p,g,h)

        if ((check_interval(x[j],q) == 3)): #s3
            x[j+1], a[j+1], b[j+1] = calculate_by_interval(3,x[j],a[j],b[j],q,p,g,h)
            if (check_interval(x[j+1],q) == 1): #s1
                x[j+2], a[j+2], b[j+2] = calculate_by_interval(1,x[j+1],a[j+1],b[j+1],q,p,g,h)
            if (check_interval(x[j+1],q) == 2): #s2
                x[j+2], a[j+2], b[j+2] = calculate_by_interval(2,x[j+1],a[j+1],b[j+1],q,p,g,h)
            if (check_interval(x[j+1],q) == 3): #s3
                x[j+2], a[j+2], b[j+2] = calculate_by_interval(3,x[j+1],a[j+1],b[j+1],q,p,g,h)

    # no solution
    return None 
# print(polars_rho(607, 101, 64, 122))
print(polars_rho(607, 101, 64, 182))
