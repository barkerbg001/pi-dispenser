import gmpy2
from gmpy2 import mpz, mpq, mpfr, get_context

def compute_pi_chudnovsky(digits):
    get_context().precision = digits * 4  # increase to reduce error
    C = 426880 * gmpy2.sqrt(10005)
    M = mpz(1)
    L = mpz(13591409)
    X = mpz(1)
    K = mpz(6)
    S = mpz(L)

    for i in range(1, digits // 14):  # each term adds ~14 digits
        M = (K**3 - 16*K) * M // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += M * L // X
        K += 12

    pi = C / S
    return str(pi)[:digits + 2]

if __name__ == "__main__":
    digits = int(input("How many digits of Pi? "))
    print("Calculating...")
    print(compute_pi_chudnovsky(digits))
