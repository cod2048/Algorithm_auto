def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    lcm_value = lcm(denom1, denom2)
    
    adjusted_numer1 = numer1 * (lcm_value // denom1)
    adjusted_numer2 = numer2 * (lcm_value // denom2)
    total_numer = adjusted_numer1 + adjusted_numer2
    
    final_gcd = gcd(total_numer, lcm_value)
    
    reduced_numer = total_numer // final_gcd
    reduced_denom = lcm_value // final_gcd
    
    return [reduced_numer, reduced_denom]
