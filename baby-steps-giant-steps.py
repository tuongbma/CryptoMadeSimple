import math

def baby_step_giant_step(p, q, g, h):
    up_rounded_sqrt_q = math.ceil(math.sqrt(q))
    baby_steps_table = {}

    # compute the baby steps
    for i in range (0, up_rounded_sqrt_q):
        baby_steps_table[(pow(g, i, p))] =  i

    # Fermat’s Little Theorem
    c = pow(g, up_rounded_sqrt_q * (p - 2), p)

    for j in range (up_rounded_sqrt_q):
        y = (h * pow(c, j, p)) % p
        if y in baby_steps_table: # if a giant-step occurs in baby-steps table
            return (baby_steps_table[y] + up_rounded_sqrt_q*j)
    
    # no result
    return None
    
# print(baby_step_giant_step(607, 101, 64, 122))
print(baby_step_giant_step(607, 101, 64, 182))